# TODO:
# * modify exports using lief
# * zero out rich header (if it exists) -->
# requires updating OptionalHeader's checksum ("Rich Header" only in Microsoft-produced executables)
# * tinker with resources: https://lief.quarkslab.com/doc/tutorials/07_pe_resource.html
# also in our project dir. : /test/lief-tutorials/PE_resource

import array
import functools
import multiprocessing
import os
import random
import signal
import string
import sys

import lief  # pip install https://github.com/lief-project/LIEF/releases/download/0.7.0/linux_lief-0.7.0_py3.6.tar.gz

module_path = os.path.split(os.path.abspath(sys.modules[__name__].__file__))[0]


# action 操作类
class MalwareManipulator(object):
    def __init__(self, bytez):
        self.bytez = bytez
        self.min_append_log2 = 5
        self.max_append_log2 = 8

    # 随机生成数据
    def __random_length(self):
        return 2 ** random.randint(self.min_append_log2, self.max_append_log2)

    # 把lief结果build成bytez
    def __binary_to_bytez(self, binary, dos_stub=False, imports=False, overlay=False, relocations=False,
                          resources=False, tls=False):
        # write the file back as bytez
        builder = lief.PE.Builder(binary)
        builder.build_dos_stub(dos_stub)  # rebuild DOS stub

        builder.build_imports(imports)  # rebuild IAT in another section
        builder.patch_imports(imports)  # patch original import table with trampolines to new import table

        builder.build_overlay(overlay)  # rebuild overlay
        builder.build_relocations(relocations)  # rebuild relocation table in another section
        builder.build_resources(resources)  # rebuild resources in another section
        builder.build_tls(tls)  # rebuilt TLS object in another section

        builder.build()  # perform the build process

        # return bytestring
        return array.array('B', builder.get_build()).tobytes()

    # append bytes to the overlay (end of PE file)
    def overlay_append(self, seed=None):
        random.seed(seed)
        L = self.__random_length()
        # choose the upper bound for a uniform distribution in [0,upper]
        upper = random.randrange(256)
        # upper chooses the upper bound on uniform distribution:
        # upper=0 would append with all 0s
        # upper=126 would append with "printable ascii"
        # upper=255 would append with any character
        return self.bytez + bytes([random.randint(0, upper) for _ in range(L)])

    # 生成随机的import name
    def generate_random_import_libname(self, minlength=5, maxlength=8):
        length = random.randint(minlength, maxlength)
        letters = string.ascii_letters + string.digits
        suffix = random.choice(['.dll', '.exe'])
        return ''.join([random.choice(letters) for _ in range(length)]) + suffix

    # 生成随机函数名
    def generate_random_name(self, minlength=5, maxlength=8):
        length = random.randint(minlength, maxlength)
        letters = string.ascii_letters + string.digits
        return ''.join([random.choice(letters) for _ in range(length)])

    # add a function to the import address table that is random name
    def imports_append(self, seed=None):
        # add (unused) imports
        random.seed(seed)
        binary = lief.PE.parse(self.bytez)
        # draw a library at random
        libname = self.generate_random_import_libname()
        funcname = self.generate_random_name()
        lowerlibname = libname.lower()
        # append this lib in the imports
        lib = binary.add_library(lowerlibname)
        lib.add_entry(funcname)

        self.bytez = self.__binary_to_bytez(binary, imports=True)

        return self.bytez

    # create a new(unused) sections
    def section_add(self, seed=None):
        random.seed(seed)
        binary = lief.PE.parse(self.bytez)
        # 建立一个section
        new_section = lief.PE.Section(self.generate_random_name())

        # fill with random content
        upper = random.randrange(256)
        L = self.__random_length()
        new_section.content = [random.randint(0, upper) for _ in range(L)]

        new_section.virtual_address = max(
            [s.virtual_address + s.size for s in binary.sections])

        # add a new empty section
        binary.add_section(new_section,
                           random.choice([
                               lief.PE.SECTION_TYPES.BSS,
                               lief.PE.SECTION_TYPES.DATA,
                               lief.PE.SECTION_TYPES.EXPORT,
                               lief.PE.SECTION_TYPES.IDATA,
                               lief.PE.SECTION_TYPES.RELOCATION,
                               lief.PE.SECTION_TYPES.RESOURCE,
                               lief.PE.SECTION_TYPES.TEXT,
                               lief.PE.SECTION_TYPES.TLS_,
                               lief.PE.SECTION_TYPES.UNKNOWN,
                           ]))

        self.bytez = self.__binary_to_bytez(binary)
        return self.bytez

    # manipulate (break) signature
    def remove_signature(self, seed=None):
        random.seed(seed)
        binary = lief.PE.parse(self.bytez)

        if binary.has_signature:
            for i, e in enumerate(binary.data_directories):
                if e.type == lief.PE.DATA_DIRECTORY.CERTIFICATE_TABLE:
                    # remove signature from certificate table
                    e.rva = 0
                    e.size = 0
                    return self.__binary_to_bytez(binary)
        # if no signature found, self.bytez is unmodified
        return self.bytez

    # manipulate debug info
    def remove_debug(self, seed=None):
        random.seed(seed)
        binary = lief.PE.parse(self.bytez)

        if binary.has_debug:
            for i, e in enumerate(binary.data_directories):
                if e.type == lief.PE.DATA_DIRECTORY.DEBUG:
                    # remove signature from certificate table
                    e.rva = 0
                    e.size = 0
                    return self.__binary_to_bytez(binary)
        # if no signature found, self.bytez is unmodified
        return self.bytez


######################
# explicitly list so that these may be used externally
ACTION_TABLE = {
    'overlay_append': 'overlay_append',
    'imports_append': 'imports_append',
    'section_add': 'section_add',
    'remove_signature': 'remove_signature',
    # 'remove_debug': 'remove_debug',
}


def modify_without_breaking(bytez, actions=[], seed=None):
    for action in actions:

        _action = ACTION_TABLE[action]

        # we run manipulation in a child process to shelter
        # our malware model from rare parsing errors in LIEF that
        # may segfault or timeout
        def helper(_action, shared_list):
            # TODO: LIEF is chatty. redirect stdout and stderr to /dev/null

            # for this process, change segfault of the child process
            # to a RuntimeEror
            def sig_handler(signum, frame):
                raise RuntimeError

            signal.signal(signal.SIGSEGV, sig_handler)

            bytez = array.array('B', shared_list[:]).tobytes()
            # TODO: LIEF is chatty. redirect output to /dev/null
            if type(_action) is str:
                _action = MalwareManipulator(bytez).__getattribute__(_action)
            else:
                _action = functools.partial(_action, bytez)

            # redirect standard out only in this queue
            try:
                shared_list[:] = _action(seed)
            except (RuntimeError, UnicodeDecodeError, TypeError, lief.not_found) as e:
                # some exceptions that have yet to be handled by public release of LIEF
                print("==== exception in child process ===")
                print(e)
                # shared_bytez remains unchanged                

        # communicate with the subprocess through a shared list
        # can't use multiprocessing.Array since the subprocess may need to
        # change the size
        manager = multiprocessing.Manager()
        shared_list = manager.list()
        shared_list[:] = bytez  # copy bytez to shared array
        # define process
        p = multiprocessing.Process(target=helper, args=(_action, shared_list))
        p.start()  # start the process
        try:
            p.join(5)  # allow this to take up to 5 seconds...
        except multiprocessing.TimeoutError:  # ..then become petulant
            print('==== timeouterror ')
            p.terminate()

        bytez = array.array('B', shared_list[:]).tobytes()  # copy result from child process

    import hashlib
    m = hashlib.sha256()
    m.update(bytez)
    return bytez


def test_overlay_append(bytez):
    binary = lief.PE.parse(bytez)
    manip = MalwareManipulator(bytez)
    bytez2 = manip.overlay_append()
    binary2 = lief.PE.parse(bytez2)
    if len(binary.overlay) == len(binary2.overlay):
        return 0
    else:
        return 1
        # assert len(binary.overlay) != len(binary2.overlay), "modification failed"


def test_imports_append(bytez):
    binary = lief.PE.parse(bytez)
    # SUCCEEDS, but note that lief builder also adds a new ".l1" section for each patch of the imports
    manip = MalwareManipulator(bytez)
    bytez2 = manip.imports_append(bytez)
    binary2 = lief.PE.parse(bytez2)
    # set1 = set(binary.imported_functions)
    # set2 = set(binary2.imported_functions)
    # diff = set2.difference(set1)
    # print(list(diff))
    if len(binary.imported_functions) == len(binary2.imported_functions):
        return 0
    else:
        return 1
        # assert len(binary.imported_functions) != len(binary2.imported_functions), "no new imported functions"


def test_section_add(bytez):
    binary = lief.PE.parse(bytez)
    manip = MalwareManipulator(bytez)
    bytez2 = manip.section_add(bytez)
    binary2 = lief.PE.parse(bytez2)
    oldsections = [s.name for s in binary.sections]
    newsections = [s.name for s in binary2.sections]
    # print(oldsections)
    # print(newsections)
    if len(newsections) == len(oldsections):
        return 0
    else:
        return 1
        # assert len(newsections) != len(oldsections), "no new sections"


def test_remove_signature(bytez):
    binary = lief.PE.parse(bytez)
    manip = MalwareManipulator(bytez)
    bytez2 = manip.remove_signature(bytez)
    binary2 = lief.PE.parse(bytez2)
    if binary.has_signature and binary2.has_signature:
        return 0
    else:
        return 1
        # assert binary2.has_signature == False, "failed to remove signature"


def test_remove_debug(bytez):
    binary = lief.PE.parse(bytez)
    manip = MalwareManipulator(bytez)
    bytez2 = manip.remove_debug(bytez)
    binary2 = lief.PE.parse(bytez2)
    if binary.has_debug and binary2.has_debug:
        return 0
    else:
        return 1
        # assert binary2.has_debug == False, "failed to remove debug"

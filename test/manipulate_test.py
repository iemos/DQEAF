import os
import lief

from gym_malware.envs.controls import manipulate2
from gym_malware.envs.controls.manipulate2 import MalwareManipulator
from gym_malware.envs.utils import interface


def testAllAction(bytez):
    def test_overlay_append(bytez):
        binary = lief.PE.parse(bytez)
        manip = MalwareManipulator(bytez)
        bytez2 = manip.overlay_append(bytez)
        binary2 = lief.PE.parse(bytez2)
        if len(binary.overlay) == len(binary2.overlay):
            return 0
        else:
            return 1
            # assert len(binary.overlay) != len(binary2.overlay), "modification failed"

    def test_imports_append(bytez):
        binary = lief.PE.parse(bytez)
        # SUCCEEDS, but note that lief builder also adds a new ".l1" section for each patch of the imports
        print('#################imports_append#################')
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

    def test_section_rename(bytez):
        binary = lief.PE.parse(bytez)
        # SUCCEEDS
        print('#################section_rename#################')
        manip = MalwareManipulator(bytez)
        bytez2 = manip.section_rename(bytez)
        binary2 = lief.PE.parse(bytez2)
        oldsections = [s.name for s in binary.sections]
        newsections = [s.name for s in binary2.sections]
        # print(oldsections)
        # print(newsections)
        if " ".join(newsections) == " ".join(oldsections):
            return 0
        else:
            return 1
            # assert " ".join(newsections) != " ".join(oldsections), "no modified sections"

    def test_section_add(bytez):
        binary = lief.PE.parse(bytez)
        print('#################section_add#################')
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

    def test_section_append(bytez):
        binary = lief.PE.parse(bytez)
        # FAILS if there's insufficient room to add to the section
        print('#################section_append#################')
        manip = MalwareManipulator(bytez)
        bytez2 = manip.section_append(bytez)
        binary2 = lief.PE.parse(bytez2)
        oldsections = [len(s.content) for s in binary.sections]
        newsections = [len(s.content) for s in binary2.sections]
        # print(oldsections)
        # print(newsections)
        if sum(newsections) == sum(oldsections):
            return 0
        else:
            return 1
            # assert sum(newsections) != sum(oldsections), "no appended section"

    def test_create_new_entry(bytez):
        binary = lief.PE.parse(bytez)
        print('#################create_new_entry#################')  # note: also adds a new section
        manip = MalwareManipulator(bytez)
        bytez2 = manip.create_new_entry(bytez)
        binary2 = lief.PE.parse(bytez2)
        # print(binary.entrypoint)
        # print(binary2.entrypoint)
        if binary.entrypoint == binary2.entrypoint:
            return 0
        else:
            return 1
            # assert binary.entrypoint != binary2.entrypoint, "no new entry point"

    def test_remove_signature(bytez):
        binary = lief.PE.parse(bytez)
        print('#################remove_signature#################')
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
        print('#################remove_debug#################')
        manip = MalwareManipulator(bytez)
        bytez2 = manip.remove_debug(bytez)
        binary2 = lief.PE.parse(bytez2)
        if binary.has_debug and binary2.has_debug:
            return 0
        else:
            return 1
            # assert binary2.has_debug == False, "failed to remove debug"

    def test_break_optional_header_checksum(bytez):
        binary = lief.PE.parse(bytez)
        print('#################break_optional_header_checksum#################')
        manip = MalwareManipulator(bytez)
        bytez2 = manip.break_optional_header_checksum(bytez)
        binary2 = lief.PE.parse(bytez2)
        if binary2.optional_header.checksum != 0:
            return 0
        else:
            return 1
            # assert binary2.optional_header.checksum == 0, "checksum not zero :("


index = 0
total = {
    "test_overlay_append": 0,
    "test_imports_append": 0,
    "test_section_rename": 0,
    "test_section_add": 0,
    "test_section_append": 0,
    "test_create_new_entry": 0,
    "test_remove_signature": 0,
    "test_remove_debug": 0,
    "test_break_optional_header_checksum": 0
}
file_list = interface.get_available_sha256()
bad_file_list = []

for sha256 in file_list:
    print("{}:[file]:{}".format(index, sha256))
    try:
        bytez = interface.fetch_file(sha256)
        if manipulate2.test_overlay_append(bytez):
            total['test_overlay_append'] += 1
        else:
            bad_file_list.append(sha256)
            continue

        if manipulate2.test_imports_append(bytez):
            total['test_imports_append'] += 1
        else:
            bad_file_list.append(sha256)
            continue

        if manipulate2.test_section_rename(bytez):
            total['test_section_rename'] += 1
        else:
            bad_file_list.append(sha256)
            continue

        if manipulate2.test_section_add(bytez):
            total['test_section_add'] += 1
        else:
            bad_file_list.append(sha256)
            continue
        # total['test_section_append'] += manipulate2.test_section_append(bytez)

        if manipulate2.test_create_new_entry(bytez):
            total['test_create_new_entry'] += 1
        else:
            bad_file_list.append(sha256)
            continue

        if manipulate2.test_remove_signature(bytez):
            total['test_remove_signature'] += 1
        else:
            bad_file_list.append(sha256)
            continue

        if manipulate2.test_remove_debug(bytez):
            total['test_remove_debug'] += 1
        else:
            bad_file_list.append(sha256)
            continue

        if manipulate2.test_break_optional_header_checksum(bytez):
            total['test_break_optional_header_checksum'] += 1
        else:
            bad_file_list.append(sha256)

    except:
        print("exception")
        bad_file_list.append(sha256)
    index += 1

# delete bad
for sha256 in bad_file_list:
    print("delete file:{}".format(sha256))
    interface.delete_file(sha256)

# sort result list
print("total:{}".format(file_list.__len__()))
for key, value in sorted(total.items(), key=lambda d: d[1]):
    print("{}:{}".format(key, value))

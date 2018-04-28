import lief

from gym_malware.envs.utils import interface
from gym_malware.envs.controls import manipulate2 as manipulate

# 从bytez字节parse，该方法只能使用lief 0.7版本
# Mac系统下使用0.8要报错，原因未知
byte = interface.fetch_file("Backdoor.Win32.PcClient.geq");
binary = lief.PE.parse(byte)
print(binary.imported_functions)

man = manipulate.MalwareManipulator(byte)
binary2 = lief.PE.parse(man.imports_append_org())
print(binary2.imported_functions)

######################
# for imported_library in binary.imports:
#     print("Library name: ", imported_library)
#     for func in imported_library.entries:
#         if not func.is_ordinal:
#             print(func.name)
#         print(func.iat_address)


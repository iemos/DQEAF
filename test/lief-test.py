import lief

from gym_malware.envs.utils import interface

# 从文件名parse
file_path = interface.get_sample_real_path("VirusShare_616a0554aa4821545c4a0aa1e89420ba")
binary = lief.parse(file_path)
print(binary)
print("-----------------------------")

# 从bytez字节parse，该方法只能使用lief 0.7版本
# Mac系统下使用0.8要报错，原因未知
binary1 = lief.PE.parse(interface.fetch_file("VirusShare_616a0554aa4821545c4a0aa1e89420ba"))
print(binary1)

######################
for imported_library in binary.imports:
    print("Library name: " + imported_library)
    for func in imported_library.entries:
        if not func.is_ordinal:
            print(func.name)
        print(func.iat_address)

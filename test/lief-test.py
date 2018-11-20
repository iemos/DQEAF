import pefile
import lief
from gym_malware.envs.utils import interface

# 从bytez字节parse，该方法只能使用lief 0.7版本
# Mac系统下使用0.8要报错，原因未知
from gym_malware.envs.utils.extractPE import extractPE



# byte = interface.fetch_file('Worm.Win32.AutoRun.sbf', test=True)
# binary = lief.PE.parse(byte)
# print(binary)
# print(extractPE().createFeature(byte))


sha_list = interface.get_available_sha256()
normal = []
unnormal = []
for sha256 in sha_list:
    bytez = interface.fetch_file(sha256)
    try:
        binary = lief.PE.parse(bytez)
        normal.append(sha256)
    except:
        unnormal.append(sha256)
        interface.delete_file(sha256)

print('normal:{}, unnormal:{}'.format(normal.__len__(), unnormal.__len__()))
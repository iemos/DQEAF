import pefile

from gym_malware.envs.utils import interface

# 从bytez字节parse，该方法只能使用lief 0.7版本
# Mac系统下使用0.8要报错，原因未知
from gym_malware.envs.utils.extractPE import extractPE

byte = interface.fetch_file("Backdoor.Win32.Hupigon.zay");
# binary = lief.PE.parse(byte)
# print(binary)
print(extractPE().createFeature(byte))

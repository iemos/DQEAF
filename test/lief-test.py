import lief

from gym_malware.envs.utils import interface
from gym_malware.envs.controls import manipulate2 as manipulate

# 从bytez字节parse，该方法只能使用lief 0.7版本
# Mac系统下使用0.8要报错，原因未知
byte = interface.fetch_file("Backdoor.Win32.Hupigon.zay");
binary = lief.PE.parse(byte)
print(binary)

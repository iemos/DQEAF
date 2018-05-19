from gym_malware.envs.utils import interface
from gym_malware.envs.utils.threedict import isPE

filename = interface.get_sample_real_path("Backdoor.Win32.Hupigon.zay")
print(isPE(filename))

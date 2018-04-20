# for local model
from gym_malware.envs.utils import interface
from gym_malware.envs.utils.pefeatures import PEFeatureExtractor

bytez = interface.fetch_file("Backdoor.Win32.PcClient.sx")
features = PEFeatureExtractor().extract(bytez)
print(features.__len__())

zero_count = 0
for item in features:
    if (item == 0):
        zero_count = zero_count + 1
print(2350 - zero_count)


# bytez = interface.fetch_file("VirusShare_0b3c009aa4e461a00c0b3755976b485e")
# # print(bytez)
# features = PEFeatureExtractor().extract(bytez)
# print(features.__len__())
# print(features)

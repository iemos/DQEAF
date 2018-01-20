# for local model
from gym_malware.envs.utils import interface
from gym_malware.envs.utils.pefeatures import PEFeatureExtractor

bytez = interface.fetch_file("VirusShare_0390d1a31da40afa7641efad8ca672d4")
# print(bytez)
features = PEFeatureExtractor().extract(bytez)
print(features.__len__())
print(features)

bytez = interface.fetch_file("VirusShare_0b3c009aa4e461a00c0b3755976b485e")
# print(bytez)
features = PEFeatureExtractor().extract(bytez)
print(features.__len__())
print(features)

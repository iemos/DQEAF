# for local model
import numpy as np

from gym_malware.envs.utils import interface
from gym_malware.envs.utils.pefeatures import PEFeatureExtractor

# bytez = interface.fetch_file("Backdoor.Win32.Hupigon.zay")
# features = PEFeatureExtractor().extract2(bytez)
# features2 = PEFeatureExtractor().extract(bytez)
# print(features.__len__())
# print(features2.__len__())

# bytez = interface.fetch_file("VirusShare_0b3c009aa4e461a00c0b3755976b485e")
# # print(bytez)
# features = PEFeatureExtractor().extract(bytez)
# print(features.__len__())
# print(features)

file_list = interface.get_available_sha256()
np.set_printoptions(threshold=1e6)

# run the tests
extractor = PEFeatureExtractor()
index = 0
for sha256 in file_list:
    print("{}:[file]:{}".format(index + 1, sha256))
    bytez = interface.fetch_file(sha256)

    index = index + 1
    print(extractor.extract2(bytez).shape)
    if index > 2:
        break

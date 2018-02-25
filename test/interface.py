# gym_malware interface hello world
from collections import defaultdict
from sklearn.model_selection import train_test_split

from gym_malware.envs.utils import interface

# 统计sample里样本组成情况
sha_list = interface.get_available_sha256()
malware = []
benign = []
for sha256 in sha_list:
    bytez = interface.fetch_file(sha256)
    label = interface.get_label_local(bytez)
    if label == 0.0:
        benign.append(sha256)
        interface.delete_file(sha256)
    else:
        malware.append(sha256)

print('malware:{}, benign:{}'.format(malware.__len__(), benign.__len__()))

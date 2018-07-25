# gym_malware interface hello world
import os
import sys

sys.path.append("..")
from gym_malware.envs.utils import interface

# # 统计sample里样本组成情况
# sha_list = interface.get_available_sha256()
# malware = []
# benign = []
# for sha256 in sha_list:
#     bytez = interface.fetch_file(sha256)
#     label = interface.get_label_local(bytez)
#     if label == 0.0:
#         benign.append(sha256)
#         interface.delete_file(sha256)
#     else:
#         malware.append(sha256)
#
# print('malware:{}, benign:{}'.format(malware.__len__(), benign.__len__()))

bytez = interface.fetch_file('Backdoor.Win32.PcClient.mzn')
label = interface.get_label_local(bytez)

print(label)

bytez = interface.fetch_evaded_file('b42a8b9411ff6171c0fbc91b42cb74c8804b9bc2f185ab9c7f238112a0ebedcb')
print(interface.get_label_local(bytez))

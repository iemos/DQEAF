# gym_malware interface hello world
from sklearn.model_selection import train_test_split

from gym_malware.envs.utils import interface

sha256 = interface.get_available_sha256()
print(sha256.__len__())

sha256_train, sha256_holdout = train_test_split(sha256, test_size=200)
print(sha256_train.__len__())
print(sha256_holdout.__len__())

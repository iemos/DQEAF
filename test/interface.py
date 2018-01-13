# gym_malware interface hello world

from gym_malware.envs.utils import interface

sha256 = interface.get_available_sha256()
print(sha256.__len__())

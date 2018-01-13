# wants to modify manipulate
from gym_malware.envs.controls import manipulate2 as manipulate
from gym_malware.envs.utils import interface

bytes = interface.fetch_file("Trojan-PSW.Win32.Mifeng.af")
manipulate.test(bytes)

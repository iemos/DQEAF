import lief
from gym_malware.envs.utils import interface

file_path = interface.get_sample_real_path("VirusShare_616a0554aa4821545c4a0aa1e89420ba")
binary = lief.parse(file_path)
print(binary.imports)

for imported_library in binary.imports:
  print("Library name: " + imported_library)
  for func in imported_library.entries:
    if not func.is_ordinal:
      print(func.name)
    print(func.iat_address)

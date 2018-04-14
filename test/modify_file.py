import sys

sys.path.append("..")
from gym_malware.envs.utils import interface
from gym_malware.envs.controls import manipulate2 as manipulate

# 本程序用于逐个运行lief修改PE文件的action，来删除不适合实验的PE文件
file_list = interface.get_available_sha256()
action_test_list = {
    'overlay_append',
    'imports_append_org',
    'section_add',
    'remove_signature'
}

# run the tests
index = 1
for sha256 in file_list:
    print("{}:原文件:{}".format(index, sha256))
    try:
        for action_name in action_test_list:
            print("使用{}动作来修改".format(action_name))
            action = manipulate.ACTION_TABLE[action_name]
            print("action{}".format(action))
            bytez = interface.fetch_file(sha256)
            bytez = bytes(manipulate.modify_without_breaking(bytez, [action]))
            with open(sha256 + "_" + action_name, 'wb') as outfile:
                outfile.write(bytez)

    except Exception as e:
        print("e{}".format(e))
    index += 1

# sort and print result list
print("total:{}".format(file_list.__len__()))

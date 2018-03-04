import sys

sys.path.append("..")
from gym_malware.envs.utils import interface
from gym_malware.envs.controls.manipulate2 import *

# 本程序用于逐个运行lief修改PE文件的action，来删除不适合实验的PE文件
file_list = interface.get_available_sha256()
action_test_dict = {
    "test_overlay_append": 0,
    "test_imports_append": 0,
    "test_section_rename": 0,
    "test_section_add": 0,
    "test_create_new_entry": 0,
    "test_remove_signature": 0,
    "test_remove_debug": 0,
    "test_break_optional_header_checksum": 0
    # "test_section_append": 0
}
bad_file_list = []

# run the tests
index = 0
for sha256 in file_list:
    print("{}:[file]:{}".format(index, sha256))
    try:
        bytez = interface.fetch_file(sha256)
        # 逐个调用测试方法
        for function_name in action_test_dict.keys():
            # 根据字符串名称 动态调用 python文件内的方法eval("function_name")(参数)
            if eval(function_name)(bytez):
                action_test_dict[function_name] += 1
            else:
                bad_file_list.append(sha256)
                break

    except Exception as e:
        print("exception")
        print(e)
        bad_file_list.append(sha256)
    index += 1

# delete bad files
for sha256 in bad_file_list:
    print("delete file:{}".format(sha256))
    interface.delete_file(sha256)

# sort and print result list
print("total:{}".format(file_list.__len__()))
for key, value in sorted(action_test_dict.items(), key=lambda d: d[1]):
    print("{}:{}".format(key, value))

from gym_malware.envs.controls import manipulate2
from gym_malware.envs.utils import interface

# 本程序用于逐个运行lief修改PE文件的action，来删除不适合实验的PE文件
total = {
    "test_overlay_append": 0,
    "test_imports_append": 0,
    "test_section_rename": 0,
    "test_section_add": 0,
    "test_section_append": 0,
    "test_create_new_entry": 0,
    "test_remove_signature": 0,
    "test_remove_debug": 0,
    "test_break_optional_header_checksum": 0
}
file_list = interface.get_available_sha256()
bad_file_list = []

# run the tests
index = 0
for sha256 in file_list:
    print("{}:[file]:{}".format(index, sha256))
    try:
        bytez = interface.fetch_file(sha256)
        if manipulate2.test_overlay_append(bytez):
            total['test_overlay_append'] += 1
        else:
            bad_file_list.append(sha256)
            continue

        if manipulate2.test_imports_append(bytez):
            total['test_imports_append'] += 1
        else:
            bad_file_list.append(sha256)
            continue

        if manipulate2.test_section_rename(bytez):
            total['test_section_rename'] += 1
        else:
            bad_file_list.append(sha256)
            continue

        if manipulate2.test_section_add(bytez):
            total['test_section_add'] += 1
        else:
            bad_file_list.append(sha256)
            continue
        # total['test_section_append'] += manipulate2.test_section_append(bytez)

        if manipulate2.test_create_new_entry(bytez):
            total['test_create_new_entry'] += 1
        else:
            bad_file_list.append(sha256)
            continue

        if manipulate2.test_remove_signature(bytez):
            total['test_remove_signature'] += 1
        else:
            bad_file_list.append(sha256)
            continue

        if manipulate2.test_remove_debug(bytez):
            total['test_remove_debug'] += 1
        else:
            bad_file_list.append(sha256)
            continue

        if manipulate2.test_break_optional_header_checksum(bytez):
            total['test_break_optional_header_checksum'] += 1
        else:
            bad_file_list.append(sha256)

    except:
        print("exception")
        bad_file_list.append(sha256)
    index += 1

# delete bad files
for sha256 in bad_file_list:
    print("delete file:{}".format(sha256))
    interface.delete_file(sha256)

# sort and print result list
print("total:{}".format(file_list.__len__()))
for key, value in sorted(total.items(), key=lambda d: d[1]):
    print("{}:{}".format(key, value))

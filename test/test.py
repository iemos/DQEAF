# 标识成功失败
import os

# 标识成功失败
dirs = os.listdir('../models/20180608T133427.173935')
# 训练提前结束，标识成功
for mm in dirs:
    # mm = str(file)
    print(mm)
    if mm.endswith('_finish') and not mm.startswith('1'):
        print(mm)

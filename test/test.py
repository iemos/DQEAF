# 标识成功失败
import os

dirs = os.listdir('logs')
# 10个txt+2个目录
if len(dirs) == 9:
    os.rename('logs', 'logs-success')

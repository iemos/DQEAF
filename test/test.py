import numpy as np


# 一维数组归一化
def oneDimNormalization(data):
    min = data.min()
    max = data.max()
    range = max - min
    return (data - min) / range


arr = np.array([2, 4, 6])
print(oneDimNormalization(arr))

print("11", "22")

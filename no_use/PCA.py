# 功能：将一字典写入到csv文件中
# 输入：文件名称，数据字典
import csv
import numpy as np
from sklearn.decomposition import PCA

from gym_malware.envs.utils import interface, pefeatures


def createDictCSV(fileName="", dataDict={}):
    with open(fileName, "w") as csvFile:
        csvWriter = csv.writer(csvFile)
        for k, v in dataDict.items():
            csvWriter.writerow([k, v])


# get scale parameters of all features
def _handle_zeros_in_scale(scale, copy=True):
    ''' Makes sure that whenever scale is zero, we handle it correctly.

    This happens in most scalers when we have constant features.'''

    # if we are fitting on 1D arrays, scale might be a scalar
    if np.isscalar(scale):
        if scale == .0:
            scale = 1.
        return scale
    elif isinstance(scale, np.ndarray):
        if copy:
            # New array to avoid side-effects
            scale = scale.copy()
        scale[scale == 0.0] = 1.0
        return scale


def MinMaxImp(X, feature_range=(0, 1)):
    data_min = np.min(X, axis=0)
    data_max = np.max(X, axis=0)
    data_range = data_max - data_min
    scale_ = ((feature_range[1] - feature_range[0]) /
              _handle_zeros_in_scale(data_range))
    min_ = feature_range[0] - data_min * scale_
    X *= scale_
    X += min_
    return X, data_min, data_max, scale_, min_


def PCA_on_training_model():
    file_list = interface.get_available_sha256()
    ex_list = np.array([pefeatures.PEFeatureExtractor().extract2(interface.fetch_file(b)) for b in file_list])
    print("all_samples: ", ex_list.shape)

    nor_list, data_min, data_max, scale_, min_ = MinMaxImp(ex_list)

    pca = PCA(n_components=0.99).fit(nor_list)
    U, S, V = pca._fit(nor_list)
    dic_elements = {"n_component": pca.n_components_}
    np.save("pca/features.npy", ex_list)
    np.save("pca/nor_features.npy", nor_list)
    np.save("pca/U.npy", U)
    np.save("pca/S.npy", S)
    np.save("pca/V.npy", V)
    np.save("pca/scale.npy", scale_)
    np.save("pca/min.npy", min_)
    createDictCSV("pca/dic_elements.csv", dic_elements)
    print("reduced dimension: ", pca.n_components_)
    return ex_list, nor_list, U, S, V


if __name__ == '__main__':
    PCA_on_training_model()

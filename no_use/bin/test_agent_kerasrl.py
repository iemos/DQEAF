import csv
from collections import defaultdict

import numpy as np
from keras.models import load_model

from gym_malware import sha256_holdout, MAXTURNS
from gym_malware.envs.controls import manipulate2 as manipulate
from gym_malware.envs.utils import interface, pefeatures

ACTION_LOOKUP = {i: act for i, act in enumerate(manipulate.ACTION_TABLE.keys())}


# 动作评估
def evaluate(action_function):
    success = []
    misclassified = []
    for sha256 in sha256_holdout:
        success_dict = defaultdict(list)
        bytez = interface.fetch_file(sha256)
        label = interface.get_label_local(bytez)
        if label == 0.0:
            misclassified.append(sha256)
            continue  # already misclassified, move along
        for _ in range(MAXTURNS):
            action = action_function(bytez)
            print(action)
            success_dict[sha256].append(action)
            bytez = manipulate.modify_without_breaking(bytez, [action])
            new_label = interface.get_label_local(bytez)
            if new_label == 0.0:
                success.append(success_dict)
                break
    return success, misclassified  # evasion accuracy is len(success) / len(sha256_holdout)


def test_models(model, score_model, test_random=False):
    total = 200
    # baseline: choose actions at random
    if test_random:
        random_action = lambda bytez: np.random.choice(list(manipulate.ACTION_TABLE.keys()))
        random_success, misclassified = evaluate(random_action)
        total = len(sha256_holdout) - len(misclassified)  # don't count misclassified towards success

    # option 1: Boltzmann sampling from Q-function network output
    softmax = lambda x: np.exp(x) / np.sum(np.exp(x))
    boltzmann_action = lambda x: np.argmax(np.random.multinomial(1, softmax(x).flatten()))
    # option 2: maximize the Q value, ignoring stochastic action space
    best_action = lambda x: np.argmax(x)

    fe = pefeatures.PEFeatureExtractor()

    def model_policy(model):
        shp = (1,) + tuple(model.input_shape[1:])

        def f(bytez):
            # first, get features from bytez
            feats = fe.extract2(bytez)
            # feats = get_ob(bytez)
            q_values = model.predict(feats.reshape(shp))[0]
            action_index = best_action(q_values)  # alternative: best_action
            return ACTION_LOOKUP[action_index]

        return f

    # compare to keras models with windowlength=1
    dqn = load_model(model)
    # dqn = load_model('models/dqn.h5')
    dqn_success, _ = evaluate(model_policy(dqn))

    dqn_score = load_model(score_model)
    # dqn_score = load_model('models/dqn_score.h5')
    score_success, _ = evaluate(model_policy(dqn_score))

    # let's compare scores
    if test_random:
        random_result = "random:{}({}/{})".format(len(random_success) / total, len(random_success), total)
    else:
        random_result = "random:untested"

    print(random_result)
    blackbox_result = "blackbox:{}({}/{})".format(len(dqn_success) / total, len(dqn_success), total)
    print(blackbox_result)
    score_result = "score:{}({}/{})".format(len(score_success) / total, len(score_success), total)
    print(score_result)
    return random_result, blackbox_result, score_result


# read csv
def readDictCSV(filename=""):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        mydict = dict(reader)
    return mydict


# scale features
def scale_min_imp(X, scale_, min_):
    X *= scale_
    X += min_
    return X


# load PCA model
def load_PCA_model():
    V = np.load("pca_models/V.npy")
    scale_ = np.load("pca_models/scale.npy")
    min_ = np.load("pca_models/min.npy")
    dic_elements = readDictCSV("pca_models/dic_elements.csv")
    pca_component = int(dic_elements['n_component'])
    return V, scale_, min_, pca_component


def compute_observation(bytez, feature_min_, V, PCA_component, feature_scale_):
    fe = pefeatures.PEFeatureExtractor()
    raw_features = fe.extract(bytez)
    # scaled_features = scale_min_imp(raw_features, feature_scale_, feature_min_)
    observation = np.dot(raw_features[np.newaxis, :], V.T[:, :PCA_component])
    return observation


def get_ob(bytez):
    V, scale_, min_, pca_component = load_PCA_model()
    ob = compute_observation(bytez, min_, V, pca_component, scale_)
    return ob

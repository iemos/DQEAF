from collections import defaultdict

import numpy as np

from gym_malware import sha256_holdout, MAXTURNS
from gym_malware.envs.controls import manipulate2 as manipulate
from gym_malware.envs.utils import interface, pefeatures

ACTION_LOOKUP = {i: act for i, act in enumerate(manipulate.ACTION_TABLE.keys())}

import gym
import os


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


# 获取保存的模型目录
def get_latest_model_dir_from(basedir):
    dirs = os.listdir(basedir)
    lastmodel = -1
    for d in dirs:
        try:
            if int(d) > lastmodel:
                lastmodel = int(d)
        except ValueError:
            continue

    assert lastmodel >= 0, "No saved models!"
    return os.path.join(basedir, str(lastmodel))


# 获取保存的模型目录，返回一个list，遇到1000_finish的情况，需要把_finish去掉
def get_model_dir_list(basedir):
    model_list = set()
    try:
        dirs = os.listdir(basedir)
    except:
        print("No saved models!")
        return model_list

    for d in dirs:
        try:
            if d != "scores.txt":
                model_list.add(os.path.join(basedir, d))
        except ValueError:
            continue

    return model_list


# 测试模型，传入两种model的路径
def test_models(model, score_model, agent_method, test_result, test_random=True, test_score=True):
    total = len(sha256_holdout)

    # baseline: choose actions at random
    if test_random:
        random_action = lambda bytez: np.random.choice(list(manipulate.ACTION_TABLE.keys()))
        random_success, misclassified = evaluate(random_action)
        total = len(sha256_holdout) - len(misclassified)  # don't count misclassified towards success

        with open(test_result, 'a+') as f:
            random_result = "random: {}({}/{})\n".format(len(random_success) / total, len(random_success), total)
            f.write(random_result)
            f.write("==========================\n")

    fe = pefeatures.PEFeatureExtractor()

    def agent_policy(agent):
        def f(bytez):
            # first, get features from bytez
            feats = fe.extract(bytez)
            action_index = agent.act(feats)
            return ACTION_LOOKUP[action_index]

        return f

    # ddqn
    env = gym.make('malware-test-v0')
    agent = agent_method(env)
    model_list = get_model_dir_list(model)
    for mm in model_list:
        agent.load(mm)
        success, _ = evaluate(agent_policy(agent))
        blackbox_result = "black: {}({}/{})".format(len(success) / total, len(success), total)
        with open(test_result, 'a+') as f:
            # 记录black各个model目录的结果
            f.write("{}->{}\n".format(mm, blackbox_result))

    with open(test_result, 'a+') as f:
        f.write("==========================\n")

    # score
    if test_score:
        env_score = gym.make('malware-score-test-v0')
        agent_score = agent_method(env_score)
        score_model_list = get_model_dir_list(score_model)
        for smm in score_model_list:
            agent_score.load(smm)
            score_success, _ = evaluate(agent_policy(agent_score))
            score_result = "score: {}({}/{})".format(len(score_success) / total, len(score_success), total)
            with open(test_result, 'a+') as f:
                f.write("{}->{}\n".format(smm, score_result))


# 测试模型，传入两种model的路径
def test_models2(model, score_model, agent_method, test_result, test_random=True, test_score=True, rounds=10000):
    total = len(sha256_holdout)

    # baseline: choose actions at random
    if test_random:
        random_action = lambda bytez: np.random.choice(list(manipulate.ACTION_TABLE.keys()))
        random_success, misclassified = evaluate(random_action)
        total = len(sha256_holdout) - len(misclassified)  # don't count misclassified towards success

        with open(test_result, 'a+') as f:
            random_result = "random: {}({}/{})\n".format(len(random_success) / total, len(random_success), total)
            f.write(random_result)
            f.write("==========================\n")

    fe = pefeatures.PEFeatureExtractor()

    def agent_policy(agent):
        def f(bytez):
            # first, get features from bytez
            feats = fe.extract(bytez)
            action_index = agent.act(feats)
            return ACTION_LOOKUP[action_index]

        return f

    # ddqn
    env = gym.make('malware-test-v0')
    agent = agent_method(env)
    mm = os.path.join(model, "{}_finish".format(rounds))
    agent.load(mm)
    success, _ = evaluate(agent_policy(agent))
    blackbox_result = "black: {}({}/{})".format(len(success) / total, len(success), total)
    with open(test_result, 'a+') as f:
        # 记录black各个model目录的结果
        f.write("{}->{}\n".format(mm, blackbox_result))

    with open(test_result, 'a+') as f:
        f.write("==========================\n")

    # score
    if test_score:
        env_score = gym.make('malware-score-test-v0')
        agent_score = agent_method(env_score)
        smm = get_latest_model_dir_from(score_model)
        agent_score.load(smm)
        score_success, _ = evaluate(agent_policy(agent_score))
        score_result = "score: {}({}/{})".format(len(score_success) / total, len(score_success), total)
        with open(test_result, 'a+') as f:
            f.write("{}->{}\n".format(smm, score_result))

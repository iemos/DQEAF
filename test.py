# coding=UTF-8
# ! /usr/bin/python
import argparse
import datetime
import os

from bin.test_agent_chainer import evaluate
from bin.train_agent_chainer import *
from bin.train_agent_chainer import create_ddqn_agent
from gym_malware import sha256_holdout
from gym_malware.envs.controls import manipulate2 as manipulate
from gym_malware.envs.utils import pefeatures

ACTION_LOOKUP = {i: act for i, act in enumerate(manipulate.ACTION_TABLE.keys())}

# 用于快速调用chainerrl的训练方法，参数如下：
# python train.py --rounds rounds(训练的次数)
model_dir = "models/"
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
parser = argparse.ArgumentParser()
parser.add_argument('--model-name', type=str, default=timestamp)
parser.add_argument('--rounds', type=int, default=50000)
parser.add_argument('--best', type=int, default=50000)
args = parser.parse_args()

model_saved_name = args.model_name
rounds = args.rounds
agent_method = create_ddqn_agent
best = args.best

model = "{}{}_{}".format(model_dir, model_saved_name, rounds)
test_result = "{}{}_{}/scores.txt".format(model_dir, model_saved_name, rounds)

# test
total = len(sha256_holdout)
fe = pefeatures.PEFeatureExtractor()


def agent_policy(agent):
    def f(bytez):
        # first, get features from bytez
        feats = fe.extract(bytez)
        action_index = agent.act(feats)
        return ACTION_LOOKUP[action_index]

    return f


env = gym.make('malware-test-v0')
agent = agent_method(env)
mm = os.path.join(model, "{}".format(best))
agent.load(mm)
success, _ = evaluate(agent_policy(agent))
blackbox_result = "black: {}({}/{})".format(len(success) / total, len(success), total)
with open(test_result, 'a+') as f:
    f.write("{}->{}\n".format(mm, blackbox_result))

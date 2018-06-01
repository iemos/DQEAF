# coding=UTF-8
# ! /usr/bin/python
import argparse
import datetime
import os

from bin.test_agent_chainer import evaluate
from bin.train_agent_chainer import *
from gym_malware import sha256_holdout
from gym_malware.envs.controls import manipulate2 as manipulate
from gym_malware.envs.utils import pefeatures

ACTION_LOOKUP = {i: act for i, act in enumerate(manipulate.ACTION_TABLE.keys())}

# 用于快速调用chainerrl的训练方法，参数如下：
# python train.py --rounds rounds(训练的次数)
model_dir = "models/"
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
parser = argparse.ArgumentParser()
parser.add_argument('--rounds', type=int, default=10000)
args = parser.parse_args()

model_saved_name = timestamp
rounds = args.rounds
agent_method = create_ddqn_agent

model = "{}{}_{}".format(model_dir, model_saved_name, rounds)
test_result = "{}{}_{}/result.txt".format(model_dir, model_saved_name, rounds)

if not os.path.exists(model):
    os.makedirs(model)

# start time
training_start_time = datetime.datetime.now()
with open(test_result, 'a+') as f:
    f.write("start->{}\n".format(training_start_time))

# black box
env, agent = train_agent(rounds=int(rounds), use_score=False, name=model, create_agent=agent_method)
with open(test_result, 'a+', encoding='utf-8') as f:
    f.write("total_turn/episode->{}({}/{})\n".format(env.total_turn / env.episode, env.total_turn, env.episode))

training_end_time = datetime.datetime.now()
with open(test_result, 'a+') as f:
    f.write("end->{}\n".format(training_end_time))

# test
# total = len(sha256_holdout)
# fe = pefeatures.PEFeatureExtractor()
#
# def agent_policy(agent):
#     def f(bytez):
#         # first, get features from bytez
#         feats = fe.extract(bytez)
#         action_index = agent.act(feats)
#         return ACTION_LOOKUP[action_index]
#
#     return f
#
# # ddqn
# success, _ = evaluate(agent_policy(agent))
# blackbox_result = "black: {}({}/{})".format(len(success) / total, len(success), total)
# with open(test_result, 'a+') as f:
#     f.write("result->{}\n".format(blackbox_result))

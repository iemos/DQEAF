#! /usr/bin/python

import argparse
import datetime

from bin.test_agent_chainer import test_models
from bin.train_agent_chainer import *
from gym_malware.envs.controls import manipulate2 as manipulate


# 用于快速调用chainerrl的训练方法，参数如下：
# python run_chainer.py --model-name name --rounds rounds --agent dqn(or acer)
# 1. 保存的模型名称
# 2. 训练的次数
# 3. 使用的创建agent方法

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
parser = argparse.ArgumentParser()
parser.add_argument('--model-name', type=str, default=timestamp)
parser.add_argument('--rounds', type=int, default=10000)
parser.add_argument('--agent', choices=['dqn', 'acer'], default='dqn')
args = parser.parse_args()

model_saved_name = args.model_name
rounds = args.rounds
if args.agent == "dqn":
    agent_method = create_ddqn_agent
else:
    agent_method = create_acer_agent

model_dir = "models/"
score_model = "{}{}_score_{}".format(model_dir, model_saved_name, rounds)
model = "{}{}_{}".format(model_dir, model_saved_name, rounds)
test_result = "{}{}_test_result.txt".format(model_dir, model_saved_name)
sub_model = "{}_finish".format(rounds)

# start time
training_start_time = datetime.datetime.now()
with open(test_result, 'a+') as f:
    f.write("training started: {}\n".format(training_start_time))

# allow graduation_agent to see scores
# train_agent(rounds=int(rounds), use_score=True, name=score_model, create_agent=agent_method)

# black blox
train_agent(rounds=int(rounds), use_score=False, name=model, create_agent=agent_method)

training_end_time = datetime.datetime.now()
with open(test_result, 'a+') as f:
    f.write("training end: {}\n".format(training_end_time))
    f.write("action:")
    for key in manipulate.ACTION_TABLE:
        f.write(key)
        f.write(',')
    f.write("\n")

# test
for i in range(3):
    with open(test_result, 'a+') as f:
        result1, result2, result3 = test_models(model, score_model, agent_method, sub_model)
        f.write("{}:{}, {}, {}\n".format(i, result1, result2, result3))

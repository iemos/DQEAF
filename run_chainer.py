#! /usr/bin/python
import argparse
import datetime

from bin.test_agent_chainer import test_models, test_models2
from bin.train_agent_chainer import *
from gym_malware.envs.controls import manipulate2 as manipulate


# 用于快速调用chainerrl的训练方法，参数如下：
# python run_chainer.py --model-name name --rounds rounds --agent dqn(or acer)
# 1. 保存的模型名称
# 2. 训练的次数
# 3. 使用的创建agent方法

model_dir = "models/"
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
parser = argparse.ArgumentParser()
parser.add_argument('--model-name', type=str, default=timestamp)
parser.add_argument('--rounds', type=int, default=7000)
parser.add_argument('--agent', choices=['dqn', 'acer'], default='dqn')
parser.add_argument('--score', type=bool, default=False)
parser.add_argument('--random', type=bool, default=True)
args = parser.parse_args()

model_saved_name = args.model_name
rounds = args.rounds
if args.agent == "dqn":
    agent_method = create_ddqn_agent
else:
    agent_method = create_acer_agent
test_score = args.score
test_random = args.random

score_model = "{}{}_score_{}".format(model_dir, model_saved_name, rounds)
model = "{}{}_{}".format(model_dir, model_saved_name, rounds)
test_result = "{}{}_test_result.txt".format(model_dir, model_saved_name)

# start time
training_start_time = datetime.datetime.now()
with open(test_result, 'a+') as f:
    f.write("start->{}\n".format(training_start_time))

# allow graduation_agent to see scores
if test_score:
    train_agent(rounds=int(rounds), use_score=True, name=score_model, create_agent=agent_method)

# black box
env = train_agent(rounds=int(rounds), use_score=False, name=model, create_agent=agent_method)
with open(test_result, 'a+', encoding='utf-8') as f:
    f.write("total_turn/episode->{}({}/{})\n".format(env.total_turn / env.episode, env.total_turn, env.episode))

training_end_time = datetime.datetime.now()
with open(test_result, 'a+') as f:
    f.write("end->{}\n".format(training_end_time))

# test
for i in range(1):
    test_models2(model, score_model, agent_method, test_result,
                 test_score=test_score, test_random=test_random, rounds=rounds)
    # test_models(model, score_model, agent_method, test_result,
    #             test_score=test_score, test_random=test_random)

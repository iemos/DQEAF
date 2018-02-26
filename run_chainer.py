#! /usr/bin/python
import argparse
import datetime

from bin.test_agent_chainer import test_models
from bin.train_agent_chainer import *

# 用于快速调用chainerrl的训练方法，参数如下：
# python run_chainer.py --model-name name --rounds rounds --agent dqn(or acer)
# 1. 保存的模型名称
# 2. 训练的次数
# 3. 使用的创建agent方法

model_dir = "models/"
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
parser = argparse.ArgumentParser()
parser.add_argument('--model-name', type=str, default=timestamp)
parser.add_argument('--rounds', type=int, default=1000)
parser.add_argument('--agent', choices=['dqn', 'acer'], default='dqn')
args = parser.parse_args()

model_saved_name = args.model_name
rounds = args.rounds
if args.agent == "dqn":
    agent_method = create_ddqn_agent
else:
    agent_method = create_acer_agent

score_model = "{}{}_score_{}".format(model_dir, model_saved_name, rounds)
model = "{}{}_{}".format(model_dir, model_saved_name, rounds)
test_result = "{}{}_test_result.txt".format(model_dir, model_saved_name)

# allow graduation_agent to see scores
train_agent(rounds=int(rounds), use_score=True, name=score_model, create_agent=agent_method)

# black blox
train_agent(rounds=int(rounds), use_score=False, name=model, create_agent=agent_method)

# test
for i in range(5):
    with open(test_result, 'a+') as f:
        result1, result2, result3 = test_models(model, score_model, agent_method)
        f.write("{}:\n".format(i))
        f.write("{}".format(result1))
        f.write("{}".format(result2))
        f.write("{}".format(result3))

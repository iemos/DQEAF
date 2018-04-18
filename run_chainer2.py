#! /usr/bin/python
import argparse
import datetime

from bin.test_agent_chainer2 import test_models
from bin.train_agent_chainer2 import *
from graduation.tools import action as manipulate

# 用于快速调用chainerrl的训练方法，参数如下：
# python run_chainer.py --model-name name --rounds rounds --agent dqn(or acer)
# 1. 保存的模型名称
# 2. 训练的次数
# 3. 使用的创建agent方法

model_dir = "models2/"
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
parser = argparse.ArgumentParser()
parser.add_argument('--model-name', type=str, default=timestamp)
parser.add_argument('--rounds', type=int, default=10000)
args = parser.parse_args()

model_saved_name = args.model_name
rounds = args.rounds
agent_method = create_ddqn_agent

score_model = "{}{}_score_{}".format(model_dir, model_saved_name, rounds)
model = "{}{}_{}".format(model_dir, model_saved_name, rounds)
test_result = "{}{}_test_result.txt".format(model_dir, model_saved_name)

# start time
training_start_time = datetime.datetime.now()

# allow graduation_agent to see scores
train_agent(rounds=int(rounds), use_score=True, name=score_model, create_agent=agent_method)

# black blox
train_agent(rounds=int(rounds), use_score=False, name=model, create_agent=agent_method)

training_end_time = datetime.datetime.now()
# 训练时间，分钟数
training_elapse = round((training_end_time - training_start_time).seconds / 60)
with open(test_result, 'a+') as f:
    f.write("训练共耗时{}分钟\n".format(training_elapse))
    f.write("action：{}\n".format(manipulate.ACTION_TABLE.keys()))

# test
for i in range(5):
    with open(test_result, 'a+') as f:
        result1, result2, result3 = test_models(model, score_model, agent_method)
        f.write("{}:\n".format(i))
        f.write("{}".format(result1))
        f.write("{}".format(result2))
        f.write("{}".format(result3))

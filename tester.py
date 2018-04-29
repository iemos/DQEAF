# encoding utf-8
#! /usr/bin/python
import argparse
import datetime

from bin.test_agent_chainer import test_models
from bin.train_agent_chainer import *

model_dir = "models/"
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
parser = argparse.ArgumentParser()
parser.add_argument('--model-name', type=str, default='201804290417')
parser.add_argument('--rounds', type=int, default=4000)
parser.add_argument('--agent', choices=['dqn', 'acer'], default='dqn')
args = parser.parse_args()

model_saved_name = args.model_name
rounds = args.rounds
if args.agent == "dqn":
    agent_method = create_ddqn_agent
else:
    agent_method = create_acer_agent

score_model = "{}{}_score_{}/{}_finish".format(model_dir, model_saved_name, rounds, rounds)
model = "{}{}_{}/{}_finish".format(model_dir, model_saved_name, rounds, rounds)
test_result = "{}{}_test_result.txt".format(model_dir, model_saved_name)

for i in range(3):
    with open(test_result, 'a+') as f:
        result1, result2, result3 = test_models(model, score_model, agent_method)
        f.write("{}:{}, {}, {}\n".format(i, result1, result2, result3))

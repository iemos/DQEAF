#! /usr/bin/python
import argparse
import datetime

from bin.test_agent_pca_chainer3 import test_models
from bin.train_agent_pca_chainer3 import *
from gym_malware.envs.controls import manipulate2 as manipulate

model_dir = "models3/"
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
parser = argparse.ArgumentParser()
parser.add_argument('--model-name', type=str, default='201804281154')
parser.add_argument('--rounds', type=int, default=5000)
args = parser.parse_args()

model_saved_name = args.model_name
rounds = args.rounds
agent_method = create_ddqn_agent

score_model = "{}{}_score_{}".format(model_dir, model_saved_name, rounds)
model = "{}{}_{}".format(model_dir, model_saved_name, rounds)
test_result = "{}{}_test_result.txt".format(model_dir, model_saved_name)

# test
for i in range(3):
    with open(test_result, 'a+') as f:
        result1, result2, result3 = test_models(model, score_model, agent_method)
        f.write("{}:{}, {}, {}\n".format(i, result1, result2, result3))

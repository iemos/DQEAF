#! /usr/bin/python
import argparse
import datetime

from no_use.bin import test_models
from no_use.bin.train_agent_pca_chainer3 import *

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
parser = argparse.ArgumentParser()
parser.add_argument('--model-name', type=str, default='201805050204')
parser.add_argument('--rounds', type=int, default=10000)
args = parser.parse_args()

model_saved_name = args.model_name
rounds = args.rounds
agent_method = create_ddqn_agent

model_dir = "models3/"
score_model = "{}{}_score_{}".format(model_dir, model_saved_name, rounds)
model = "{}{}_{}".format(model_dir, model_saved_name, rounds)
test_result = "{}{}_test_result.txt".format(model_dir, model_saved_name)

# test
for i in range(1):
    test_models(model, score_model, agent_method, test_result)

#! /usr/bin/python
import argparse
import datetime

from no_use.bin import test_models
from no_use.bin.train_agent_pca_chainer3 import *
from gym_malware.envs.controls import manipulate2 as manipulate

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
parser = argparse.ArgumentParser()
parser.add_argument('--model-name', type=str, default=timestamp)
parser.add_argument('--rounds', type=int, default=5000)
args = parser.parse_args()

model_saved_name = args.model_name
rounds = args.rounds
agent_method = create_ddqn_agent

model_dir = "models3/"
score_model = "{}{}_score_{}".format(model_dir, model_saved_name, rounds)
model = "{}{}_{}".format(model_dir, model_saved_name, rounds)
test_result = "{}{}_test_result.txt".format(model_dir, model_saved_name)

# start time
training_start_time = datetime.datetime.now()
with open(test_result, 'a+') as f:
    f.write("start->{}\n".format(training_start_time))
    f.write("action：{}\n".format(manipulate.ACTION_TABLE.keys()))

# allow graduation_agent to see scores
train_agent(rounds=int(rounds), use_score=True, name=score_model, create_agent=agent_method)

# black blox
train_agent(rounds=int(rounds), use_score=False, name=model, create_agent=agent_method)

training_end_time = datetime.datetime.now()
with open(test_result, 'a+') as f:
    f.write("end->{}\n".format(training_end_time))

# test
for i in range(1):
    test_models(model, score_model, agent_method, test_result)

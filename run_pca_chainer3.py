#! /usr/bin/python
import argparse
import datetime

from bin.test_agent_pca_chainer3 import test_models
from bin.train_agent_pca_chainer3 import *
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
sub_model = "/{}_finish".format(rounds)

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

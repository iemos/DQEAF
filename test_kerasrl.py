import argparse
import datetime

import pickle

from bin.test_agent_kerasrl import test_models
from bin.train_agent_kerasrl import train_dqn_model
from gym_malware.envs.controls import manipulate2 as manipulate

# timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
timestamp = '201805130852'
parser = argparse.ArgumentParser()
parser.add_argument('--rounds', type=int, default=10000)
args = parser.parse_args()

rounds = args.rounds

model_name = 'models/kerasrl_{}_{}.h5'.format(timestamp, rounds)
test_result = "models/kerasrl_{}_{}.txt".format(timestamp, rounds)

# test
for i in range(1):
    with open(test_result, 'a+') as f:
        result1, result2, result3 = test_models(model_name, '')
        f.write("{}:{}, {}, {}\n".format(i, result1, result2, result3))

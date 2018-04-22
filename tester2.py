# encoding utf-8
# ! /usr/bin/python
import argparse
import datetime

from bin.test_agent_chainer2 import test_models
from bin.train_agent_chainer2 import *

model_dir = "models2/"
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
parser = argparse.ArgumentParser()
parser.add_argument('--model-name', type=str, default='201804210243')
parser.add_argument('--rounds', type=int, default=10000)
args = parser.parse_args()

model_saved_name = args.model_name
rounds = args.rounds
agent_method = create_ddqn_agent

score_model = "{}{}_score_{}".format(model_dir, model_saved_name, rounds)
model = "{}{}_{}".format(model_dir, model_saved_name, rounds)
test_result = "{}{}_test_result.txt".format(model_dir, model_saved_name)

for i in range(5):
    with open(test_result, 'a+') as f:
        result1, result2, result3 = test_models(model, score_model, agent_method)
        f.write("{}:\n".format(i))
        f.write("{}".format(result1))
        f.write("{}".format(result2))
        f.write("{}".format(result3))

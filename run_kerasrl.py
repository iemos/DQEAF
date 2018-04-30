import argparse
import datetime

import pickle

from bin.test_agent_kerasrl import test_models
from bin.train_agent_kerasrl import train_dqn_model
from gym_malware.envs.controls import manipulate2 as manipulate

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
parser = argparse.ArgumentParser()
parser.add_argument('--model-name', type=str, default=timestamp)
parser.add_argument('--rounds', type=int, default=10000)
args = parser.parse_args()

model_saved_name = args.model_name
rounds = args.rounds

model_name = 'models/kerasrl_{}_{}.h5'.format(timestamp, rounds)
test_result = "models/kerasrl_{}_{}.txt".format(timestamp, rounds)

# start time
training_start_time = datetime.datetime.now()
with open(test_result, 'a+') as f:
    f.write("training started: {}\n".format(training_start_time))

# black blox
agent1, model1, history_train1, history_test1 = train_dqn_model([1024, 256], rounds=rounds, run_test=True,
                                                                use_score=False)  # black blox
model1.save(model_name, overwrite=True)
with open('history_blackbox_{}_{}.pickle'.format(timestamp, rounds), 'wb') as f:
    pickle.dump(history_test1, f, pickle.HIGHEST_PROTOCOL)

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
        result1, result2, result3 = test_models(model_name, '', False)
        f.write("{}:{}, {}, {}\n".format(i, result1, result2, result3))

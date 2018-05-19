import argparse
import datetime

from bin.test_agent_kerasrl import test_models
from bin.train_agent_kerasrl import train_dqn_model_EpsGreedy_Policy

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
parser = argparse.ArgumentParser()
parser.add_argument('--rounds', type=int, default=10000)
args = parser.parse_args()

rounds = args.rounds

model_name = 'kerasrl/{}_{}.h5'.format(timestamp, rounds)
model_score_name = 'kerasrl/score_{}_{}.h5'.format(timestamp, rounds)
test_result = "kerasrl/{}_{}.txt".format(timestamp, rounds)

# start time
training_start_time = datetime.datetime.now()
with open(test_result, 'a+') as f:
    f.write("training started: {}\n".format(training_start_time))

# black blox
_, model1, _, _ = train_dqn_model_EpsGreedy_Policy([256, 256, 256], rounds=rounds)  # black box
model1.save(model_name, overwrite=True)

# with open('history_blackbox_{}_{}.pickle'.format(timestamp, rounds), 'wb') as f:
#     pickle.dump(history_test1, f, pickle.HIGHEST_PROTOCOL)

_, model2, _, _ = train_dqn_model_EpsGreedy_Policy([256, 256, 256], rounds=rounds, use_score=True)  # score
model2.save(model_score_name, overwrite=True)

training_end_time = datetime.datetime.now()
with open(test_result, 'a+') as f:
    f.write("training end: {}\n".format(training_end_time))

# test
for i in range(2):
    with open(test_result, 'a+') as f:
        result1, result2, result3 = test_models(model_name, model_score_name, True)
        f.write("{}:{}, {}, {}\n".format(i, result1, result2, result3))

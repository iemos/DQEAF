import argparse

from bin.test_agent_kerasrl import test_models

# timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
timestamp = '201805132111'
parser = argparse.ArgumentParser()
parser.add_argument('--rounds', type=int, default=5000)
args = parser.parse_args()

rounds = args.rounds

model_name = 'kerasrl/{}_{}.h5'.format(timestamp, rounds)
model_score_name = 'kerasrl/score_{}_{}.h5'.format(timestamp, rounds)
test_result = "kerasrl/{}_{}.txt".format(timestamp, rounds)

# test
for i in range(1):
    with open(test_result, 'a+') as f:
        result1, result2, result3 = test_models(model_name, model_score_name, True)
        f.write("{}:{}, {}, {}\n".format(i, result1, result2, result3))

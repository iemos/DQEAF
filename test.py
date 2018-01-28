import sys

from bin.test_agent_chainer import test_models

model = "models/create_ddqn_agent"
score_model = model + "_score"
try:
    rounds = sys.argv[1]
    model += "_" + rounds
    score_model += "_" + rounds
except:
    print("you need to input the training rounds!")

test_models(model, score_model)

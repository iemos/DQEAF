import sys

from bin.test_agent_chainer import test_models

model = "models/create_ddqn_agent_"
score_model = model + "score_"
try:
    rounds = sys.argv[1]
    model += rounds
    score_model += rounds

    test_models(model, score_model)
except Exception as e:
    print(e)
    print("you need to enter the training rounds!")

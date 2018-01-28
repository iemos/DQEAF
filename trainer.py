from bin.train_agent_chainer import train_agent
import sys

model_dir = "models/"
try:
    agent_name = sys.argv[1]
    rounds = sys.argv[2]
    score_model = model_dir + agent_name + "_score_" + rounds
    model = model_dir + agent_name + "_" + rounds

    # allow graduation_agent to see scores
    train_agent(rounds=rounds, use_score=True, name=score_model, create_agent=eval(agent_name))

    # black blox
    train_agent(rounds=rounds, use_score=False, name=model, create_agent=eval(agent_name))
except Exception as e:
    print(e)
    print("you need to enter the training rounds and the agent you use!")

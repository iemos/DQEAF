from bin.train_agent_chainer import *
import sys


# 获取命令行参数
def get_args(argv):
    model_saved_name = "model_saved_name"
    rounds = 50000
    agent_method = create_ddqn_agent

    arg_length = argv.__len__()
    # 必须输入四个参数，否则使用默认设置
    if arg_length == 4:
        model_saved_name = argv[1]
        rounds = argv[2]
        agent_method = argv[3]

    return model_saved_name, rounds, agent_method


model_dir = "models/"
model_saved_name, rounds, agent_method = get_args(sys.argv)

score_model = model_dir + model_saved_name + "_score_{}".format(rounds)
model = model_dir + model_saved_name + "_{}".format(rounds)

# allow graduation_agent to see scores
train_agent(rounds=rounds, use_score=True, name=score_model, create_agent=agent_method)

# black blox
train_agent(rounds=rounds, use_score=False, name=model, create_agent=agent_method)

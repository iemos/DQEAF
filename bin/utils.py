from bin.train_agent_chainer import *


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
        if argv[3] == "dqn":
            agent_method = create_ddqn_agent
        elif argv[3] == "acer":
            agent_method = create_acer_agent
        else:
            print("wrong agent method!")

    return model_saved_name, rounds, agent_method

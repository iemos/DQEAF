#! /usr/bin/python

import sys
from bin.test_agent_chainer import test_models

def get_args(argv):
    model_saved_name = "model_saved_name"
    rounds = 50000

    arg_length = argv.__len__()
    # 必须输入四个参数，否则使用默认设置
    if arg_length == 3:
        model_saved_name = argv[1]
        rounds = argv[2]

    return model_saved_name, rounds


model_dir = "models/"
model_saved_name, rounds = get_args(sys.argv)

score_model = "{}{}_score_{}".format(model_dir, model_saved_name, rounds)
model = "{}{}_{}".format(model_dir, model_saved_name, rounds)

test_models(model, score_model)

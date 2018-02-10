#! /usr/bin/python
from bin.train_agent_chainer import *
import bin.utils as util
import sys

# 用于快速调用chainerrl的训练方法，参数如下：
# python trainer.py name rounds dqn(or acer)
# 1. 保存的模型名称
# 2. 训练的次数
# 3. 使用的创建agent方法

model_dir = "models/"
model_saved_name, rounds, agent_method = util.get_args3(sys.argv)

score_model = "{}{}_score_{}".format(model_dir, model_saved_name, rounds)
model = "{}{}_{}".format(model_dir, model_saved_name, rounds)

# allow graduation_agent to see scores
train_agent(rounds=int(rounds), use_score=True, name=score_model, create_agent=agent_method)

# black blox
train_agent(rounds=int(rounds), use_score=False, name=model, create_agent=agent_method)
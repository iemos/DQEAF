#! /usr/bin/python

import sys
from bin.test_agent_chainer import test_models
import bin.utils as util


model_dir = "models/"
model_saved_name, rounds, agent_method = util.get_args3(sys.argv)

score_model = "{}{}_score_{}".format(model_dir, model_saved_name, rounds)
model = "{}{}_{}".format(model_dir, model_saved_name, rounds)

test_models(model, score_model, agent_method)

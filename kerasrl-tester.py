#! /usr/bin/python

import sys
from bin.test_agent_kerasrl import test_models
import bin.utils as util

model_dir = "models/"
model_saved_name = util.get_args(sys.argv)

score_model = "{}{}_score.h5".format(model_dir, model_saved_name)
model = "{}{}.h5".format(model_dir, model_saved_name)

test_models(model, score_model)

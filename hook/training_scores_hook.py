from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

import visdom
from chainerrl.experiments import StepHook


class TrainingScoresHook(StepHook):
    def __init__(self, title, outdir, figsize=(600, 400)):
        self.outdir = outdir
        self.textwindow = None
        self.opts = dict(
            showlegend=True,
            width=figsize[0],
            height=figsize[1],
            title=title
        )

        self.vis = visdom.Visdom(port=8888)
        assert self.vis.check_connection(), "Fail to connect to Visdom backend!"

    def text(self):
        with open(os.path.join(self.outdir, 'scores.txt'), 'r') as f:
            content = f.read()
            if self.textwindow is None:
                self.textwindow = self.vis.text(content, opts=self.opts)
            else:
                self.vis.text(content, win=self.textwindow)

    def __call__(self, env, agent, step):
        if step % 100 == 0:
            self.text()

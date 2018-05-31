import numpy as np
import visdom

vis = visdom.Visdom(port=8888)
assert vis.check_connection(), "Fail to connect to Visdom backend!"


class StepSignature(object):
    def __init__(self, title, xlabel='x', ylabel='y',
                 figsize=(440, 400), margin=(40, 40, 30, 30), fillarea=False):
        self.win = None
        self.opts = dict(
            fillarea=fillarea,
            showlegend=True,
            width=figsize[0],
            height=figsize[1],
            xlabel=xlabel,
            ylabel=ylabel,
            title=title,
            marginleft=margin[0],
            marginright=margin[1],
            margintop=margin[2],
            marginbottom=margin[3])

    def plot(self, step: int, sig: dict):
        '''Iterative plot
        example: ss.plot(i, dict(a=i*i, b=51-3*i))
        '''
        X = np.array([[step] * len(sig.keys())])
        Y = np.array([[sig[k] for k in sig.keys()]])
        self.opts['legend'] = list(sig.keys())
        if self.win is None:
            self.win = vis.line(Y=Y, X=X, opts=self.opts)
        else:
            vis.line(Y=Y, X=X, win=self.win, update='append', opts=self.opts)

# __all__ = ['StepSignature']
#
# if __name__ == "__main__":
#     ss = StepSignature('hello')
#     for i in range(4):
#         ss.plot(i, dict(a=i * i, b=51 - 3 * i))

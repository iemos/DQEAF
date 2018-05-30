## 用Visdom画loss曲线

#### 1. 启用Visdom服务

* 用pip安装visdom后，执行：

```
python -m visdom.server -port=你设置的端口
```

> 我是将visdom服务建在screen里面，再用putty建了一个ssh的tunnel来查看绘图。目前我用了默认端口8097。若不另设置端口，将绘制到我所用的visdom页面。

#### 2. 画loss曲线

代码如下:

```python
# step_signature.py
import visdom
import numpy as np

vis = visdom.Visdom()
assert vis.check_connection(), "Fail to connect to Visdom backend!"
    
class StepSignature(object):
    def __init__(self, title, xlabel='x', ylabel='y', 
                 figsize=(440,400), margin=(40,40,30,30), fillarea=False):
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
    
    def plot(self, step:int, sig:dict):
        '''Iterative plot
        example: ss.plot(i, dict(a=i*i, b=51-3*i))
        '''
        X = np.array([[step] * len(sig.keys())])
        Y = np.array([[sig[k] for k in sig.keys()]])
        self.opts['legend']=list(sig.keys())
        if self.win is None:
            self.win = vis.line(Y=Y, X=X, opts=self.opts)
        else:
            vis.line(Y=Y, X=X, win=self.win, update='append', opts=self.opts)
        
__all__ = ['StepSignature']

if __name__ == "__main__":
    ss = StepSignature('hello')
    for i in range(10):
        ss.plot(i, dict(a=i*i, b=51-3*i))
```

其中，最关键是调用以下两步：

```python
ss = StepSignature('hello') # 初始化窗口信息
ss.plot(i, dict(loss=loss_i)) # 更新绘制loss曲线
```

如果有多条loss曲线，则只需更改参数2：`ss.plot(i, dict(loss1=i*i, loss2=51-3i))`。
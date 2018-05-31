# import matplotlib.pyplot as plt
#
# x = [1,2,3]
# y = [5,7,4]
#
# x2 = [1,2,3]
# y2 = [10,14,12]
#
# plt.plot(x, y, label='First Line')
# plt.plot(x2, y2, label='Second Line')
#
# plt.xlabel('Plot Number')
# plt.ylabel('Important var')
# plt.title('Interesting Graph\nCheck it out')
# plt.legend()
# plt.show()
#
# import numpy as np
# from visdom import Visdom
#
# # line plots
# viz = Visdom()
# viz.line(Y=np.random.rand(10), opts=dict(showlegend=True))
#
# Y = np.linspace(-5, 5, 100)
# viz.line(
#     Y=np.column_stack((Y * Y, np.sqrt(Y + 5))),
#     X=np.column_stack((Y, Y)),
#     opts=dict(markers=False),
# )
#
# # line updates
# win = viz.line(
#     X=np.column_stack((np.arange(0, 10), np.arange(0, 10))),
#     Y=np.column_stack((np.linspace(5, 10, 10),
#                        np.linspace(5, 10, 10) + 5)),
# )
# viz.line(
#     X=np.column_stack((np.arange(10, 20), np.arange(10, 20))),
#     Y=np.column_stack((np.linspace(5, 10, 10),
#                        np.linspace(5, 10, 10) + 5)),
#     win=win,
#     update='append'
# )
# viz.line(
#     X=np.arange(21, 30),
#     Y=np.arange(1, 10),
#     win=win,
#     name='2',
#     update='append'
# )
# viz.line(
#     X=np.arange(1, 10),
#     Y=np.arange(11, 20),
#     win=win,
#     name='delete this',
#     update='append'
# )
# viz.line(
#     X=np.arange(1, 10),
#     Y=np.arange(11, 20),
#     win=win,
#     name='4',
#     update='insert'
# )
# viz.line(X=None, Y=None, win=win, name='delete this', update='remove')
#
# Y = np.linspace(0, 4, 200)
# win = viz.line(
#     Y=np.column_stack((np.sqrt(Y), np.sqrt(Y) + 2)),
#     X=np.column_stack((Y, Y)),
#     opts=dict(
#         fillarea=True,
#         showlegend=False,
#         width=800,
#         height=800,
#         xlabel='Time',
#         ylabel='Volume',
#         ytype='log',
#         title='Stacked area plot',
#         marginleft=30,
#         marginright=30,
#         marginbottom=80,
#         margintop=30,
#     ),
# )
#
# # Assure that the stacked area plot isn't giant
# viz.update_window_opts(
#     win=win,
#     opts=dict(
#         width=300,
#         height=300,
#     ),
# )

tup = [('a', 11), ('b', 22)]
print(tup[1][1])

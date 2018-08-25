net = []
n_hidden_channels = [1024, 256]
inpdim = 4
for i, n_hid in enumerate(n_hidden_channels):
    net += [('l{}'.format(i), inpdim, n_hid)]
    net += [('norm{}'.format(i), n_hid)]
    net += [('_act{}'.format(i), 0)]
print(net)

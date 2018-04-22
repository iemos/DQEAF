import chainer
import chainer.functions as F
import chainer.links as L
import chainerrl
import gym
import numpy as np


class QFunction(chainer.Chain):
    def __init__(self, obs_size, n_actions, n_hidden_channels=[1024, 256]):
        super(QFunction, self).__init__()
        net = []
        inpdim = obs_size
        for i, n_hid in enumerate(n_hidden_channels):
            # [2350, 1024]
            net += [('l{}'.format(i), L.Linear(inpdim, n_hid))]
            net += [('norm{}'.format(i), L.BatchNormalization(n_hid))]
            net += [('_act{}'.format(i), F.relu)]
            inpdim = n_hid

        net += [('output', L.Linear(inpdim, n_actions))]

        with self.init_scope():
            for n in net:
                if not n[0].startswith('_'):
                    setattr(self, n[0], n[1])

        self.forward = net

    def __call__(self, x, test=False):
        """
        Args:
            x (ndarray or chainer.Variable): An observation
            test (bool): a flag indicating whether it is in test mode
        """
        for n, f in self.forward:
            if not n.startswith('_'):
                x = getattr(self, n)(x)
            else:
                x = f(x)

        return chainerrl.action_value.DiscreteActionValue(x)


# 创建ddqn agent
def create_ddqn_agent(env):
    obs_dim = env.observation_space.shape[0]
    n_actions = env.action_space.n

    q_func = QFunction(obs_dim, n_actions)
    # q_func.to_gpu(0)

    optimizer = chainer.optimizers.Adam(eps=1e-2)
    optimizer.setup(q_func)

    # Set the discount factor that discounts future rewards.
    gamma = 0.95

    # Use epsilon-greedy for exploration
    explorer = chainerrl.explorers.Boltzmann()
    # explorer = chainerrl.explorers.ConstantEpsilonGreedy(
    #     epsilon=0.3, random_action_func=env.action_space.sample)

    # DQN uses Experience Replay.
    # Specify a replay buffer and its capacity.
    replay_buffer = chainerrl.replay_buffer.ReplayBuffer(capacity=1000)

    # Chainer only accepts numpy.float32 by default, make sure
    # a converter as a feature extractor function phi.
    phi = lambda x: x.astype(np.float32, copy=False)

    # Now create an graduation_agent that will interact with the environment.
    # DQN graduation_agent as described in Mnih (2013) and Mnih (2015).
    # http://arxiv.org/pdf/1312.5602.pdf
    # http://arxiv.org/abs/1509.06461        
    agent = chainerrl.agents.DoubleDQN(
        q_func, optimizer, replay_buffer, gamma, explorer,
        replay_start_size=32, update_interval=1,
        target_update_interval=100, phi=phi)

    return agent


# 开始训练
def train_agent(rounds=10000, use_score=False, name='result_dir', create_agent=create_ddqn_agent):
    ENV_NAME = 'malware-score-v0' if use_score else 'malware-v0'
    env = gym.make(ENV_NAME)
    np.random.seed(123)
    env.seed(123)

    agent = create_agent(env)

    chainerrl.experiments.train_agent_with_evaluation(
        agent, env,
        steps=rounds,  # Train the graduation_agent for this many rounds steps
        max_episode_len=env.maxturns,  # Maximum length of each episodes
        eval_interval=1000,  # Evaluate the graduation_agent after every 1000 steps
        eval_n_runs=100,  # 100 episodes are sampled for each evaluation
        outdir=name)  # Save everything to 'result' directory

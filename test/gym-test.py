# gym hello world
import chainer
import chainer.functions as F
import chainer.links as L
import chainerrl
import gym
import numpy as np

env = gym.make('CartPole-v0')


def createAgentDQN():
    class QFunction(chainer.Chain):
        def __init__(self, obs_size, n_actions, n_hidden_channels=50):
            super().__init__()
            with self.init_scope():
                self.l0 = L.Linear(obs_size, n_hidden_channels)
                self.l1 = L.Linear(n_hidden_channels, n_hidden_channels)
                self.l2 = L.Linear(n_hidden_channels, n_actions)

        def __call__(self, x, test=False):
            """
            Args:
                x (ndarray or chainer.Variable): An observation
                test (bool): a flag indicating whether it is in test mode
            """
            h = F.tanh(self.l0(x))
            h = F.tanh(self.l1(h))
            return chainerrl.action_value.DiscreteActionValue(self.l2(h))

    obs_size = env.observation_space.shape[0]
    n_actions = env.action_space.n
    q_func = QFunction(obs_size, n_actions)
    # use ChainerRL's predefined Q-functions
    # q_func = chainerrl.q_functions.FCStateQFunctionWithDiscreteAction(
    #     obs_size, n_actions,
    #     n_hidden_layers=2, n_hidden_channels=50)
    # q_func.to_gpu()
    # Use Adam to optimize q_func. eps=1e-2 is for stability.
    optimizer = chainer.optimizers.Adam(eps=1e-2)
    optimizer.setup(q_func)

    # Set the discount factor that discounts future rewards.
    gamma = 0.95

    # Use epsilon-greedy for exploration
    explorer = chainerrl.explorers.ConstantEpsilonGreedy(
        epsilon=0.3, random_action_func=env.action_space.sample)

    # DQN uses Experience Replay.
    # Specify a replay buffer and its capacity.
    replay_buffer = chainerrl.replay_buffer.ReplayBuffer(capacity=10 ** 6)

    # Since observations from CartPole-v0 is numpy.float64 while
    # Chainer only accepts numpy.float32 by default, specify
    # a converter as a feature extractor function phi.
    phi = lambda x: x.astype(np.float32, copy=False)

    # Now create an graduation_agent that will interact with the environment.
    agent = chainerrl.agents.DoubleDQN(
        q_func, optimizer, replay_buffer, gamma, explorer,
        replay_start_size=500, update_interval=1,
        target_update_interval=100, phi=phi)

    return agent


class randomAgent():
    """The world's simplest graduation_agent!"""

    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation):
        return self.action_space.sample()

    def stop_episode(self):
        pass


agent = createAgentDQN()
agent.load("cart")
# graduation_agent = randomAgent(env.action_space)


for i_episode in range(10):
    observation = env.reset()
    R = 0
    for t in range(300):
        env.render()
        action = agent.act(observation)
        observation, reward, done, info = env.step(action)
        R += reward
        if done:
            print("{}:Episode finished after {} timesteps, reward {}".format(i_episode, t + 1, R))
            break
    agent.stop_episode()

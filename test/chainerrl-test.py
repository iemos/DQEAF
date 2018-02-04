import chainer
import chainer.functions as F
import chainer.links as L
import chainerrl
import gym
import numpy as np


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


env = gym.make('CartPole-v0')
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

# # train agent
# n_episodes = 300
# max_episode_len = 200
# for i in range(1, n_episodes + 1):
#     obs = env.reset()
#     reward = 0
#     done = False
#     R = 0  # return (sum of rewards)
#     t = 0  # time step
#     while not done and t < max_episode_len:
#         # Uncomment to watch the behaviour
#         # env.render()
#         action = agent.act_and_train(obs, reward)
#         obs, reward, done, _ = env.step(action)
#         R += reward
#         t += 1
#     if i % 10 == 0:
#         print('episode:', i,
#               'R:', R)
#     agent.stop_episode_and_train(obs, reward, done)
# print('Agent Finished.')
#
# # test agent
# for i in range(10):
#     obs = env.reset()
#     done = False
#     R = 0
#     t = 0
#     while not done and t < max_episode_len:
# #        env.render()
#         action = agent.act(obs)
#         obs, r, done, _ = env.step(action)
#         R += r
#         t += 1
#     print('test episode:', i, 'R:', R)
#     agent.stop_episode()
# print('RL completed!')
#
# agent.save("cart")
# print("Agent cart saved!")


# Set up the logger to print info messages for understandability.
import logging
import sys

gym.undo_logger_setup()  # Turn off gym's default logger settings
logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='')

chainerrl.experiments.train_agent_with_evaluation(
    agent, env,
    steps=2000,  # Train the graduation_agent for 2000 steps
    eval_n_runs=10,  # 10 episodes are sampled for each evaluation
    max_episode_len=200,  # Maximum length of each episodes
    eval_interval=1000,  # Evaluate the graduation_agent after every 1000 steps
    outdir='result')  # Save everything to 'result' directory

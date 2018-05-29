"""
The DQN improvement: Prioritized Experience Replay (based on https://arxiv.org/abs/1511.05952)

View more on my tutorial page: https://morvanzhou.github.io/tutorials/

Using:
Tensorflow: 1.0
gym: 0.8.0
"""

import datetime
import os
from collections import defaultdict

import gym
import numpy as np
# import matplotlib.pyplot as plt
import tensorflow as tf

from gym_malware import sha256_holdout, MAXTURNS
from gym_malware.envs.controls import manipulate2 as manipulate
from gym_malware.envs.utils import interface, pefeatures
from new_dir.RL_brain import DQNPrioritizedReplay

TRAIN_EPISODE = 1000
env = gym.make('malware-v0')
env = env.unwrapped
env.seed(21)
MEMORY_SIZE = 10000
ACTION_LOOKUP = {i: act for i, act in enumerate(manipulate.ACTION_TABLE.keys())}

sess = tf.Session()
# with tf.variable_scope('natural_DQN'):
#     RL_natural = DQNPrioritizedReplay(
#         n_actions=3, n_features=2, memory_size=MEMORY_SIZE,
#         e_greedy_increment=0.00005, sess=sess, prioritized=False,
#     )

with tf.variable_scope('DQN_with_prioritized_replay'):
    RL_prio = DQNPrioritizedReplay(
        n_actions=4, n_features=2350, memory_size=MEMORY_SIZE,
        e_greedy_increment=0.00005, sess=sess, prioritized=True, output_graph=True,
    )
sess.run(tf.global_variables_initializer())


def train(RL):
    total_steps = 0
    steps = []
    episodes = []
    for i_episode in range(TRAIN_EPISODE):
        observation = env.reset()
        while True:
            # env.render()

            action = RL.choose_action(observation)

            observation_, reward, done, info = env.step(action)

            if done: reward = 10
            print("reward: ", reward)

            RL.store_transition(observation, action, reward, observation_)

            if total_steps > MEMORY_SIZE:
                RL.learn()

            if done:
                print('episode ', i_episode, ' finished')
                steps.append(total_steps)
                episodes.append(i_episode)
                break

            observation = observation_
            total_steps += 1
    return np.vstack((episodes, steps))


# 动作评估
def evaluate(action_function):
    success = []
    misclassified = []
    for sha256 in sha256_holdout:
        success_dict = defaultdict(list)
        bytez = interface.fetch_file(sha256)
        label = interface.get_label_local(bytez)
        if label == 0.0:
            misclassified.append(sha256)
            continue  # already misclassified, move along
        for _ in range(MAXTURNS):
            action = action_function(bytez)
            print(action)
            success_dict[sha256].append(action)
            bytez = manipulate.modify_without_breaking(bytez, [action])
            new_label = interface.get_label_local(bytez)
            if new_label == 0.0:
                success.append(success_dict)
                break
    return success, misclassified  # evasion accuracy is len(success) / len(sha256_holdout)


# 测试模型
def tt_models(RL, test_result, test_random=True):
    total = len(sha256_holdout)

    # baseline: choose actions at random
    if test_random:
        random_action = lambda bytez: np.random.choice(list(manipulate.ACTION_TABLE.keys()))
        random_success, misclassified = evaluate(random_action)
        total = len(sha256_holdout) - len(misclassified)  # don't count misclassified towards success

        with open(test_result, 'a+') as f:
            random_result = "random: {}({}/{})\n".format(len(random_success) / total, len(random_success), total)
            f.write(random_result)
            f.write("===========\n")

    fe = pefeatures.PEFeatureExtractor()

    def agent_policy(agent):
        def f(bytez):
            # first, get features from bytez
            feats = fe.extract(bytez)
            action_index = agent.act(feats)
            return ACTION_LOOKUP[action_index]

        return f

    # ddqn
    # env = gym.make('malware-test-v0')
    print("black box")

    success, _ = evaluate(agent_policy(RL))
    blackbox_result = "black: {}({}/{})".format(len(success) / total, len(success), total)
    with open(test_result, 'a+') as f:
        # 记录black各个model目录的结果
        f.write("{}\n".format(blackbox_result))

    with open(test_result, 'a+') as f:
        f.write("==========================\n")


if not os.path.exists("Model"):
    os.makedirs("Model")

test_result = "{}{}_test_result.txt".format("Model/", "1")

saver = tf.train.Saver()
# start time
training_start_time = datetime.datetime.now()
with open(test_result, 'a+') as f:
    f.write("start->{}\n".format(training_start_time))
# his_natural = train(RL_natural)
his_prio = train(RL_prio)

saver.save(sess, "Model/model.ckpt")
with open(test_result, 'a+', encoding='utf-8') as f:
    f.write("total_turn->{}\n".format(env.total_turn))
    f.write("episode->{}\n".format(env.episode))
    f.write("{}\n".format(env.total_turn / env.episode))

training_end_time = datetime.datetime.now()
with open(test_result, 'a+') as f:
    f.write("end->{}\n".format(training_end_time))

# model_file=tf.train.latest_checkpoint('ckpt/')
saver.restore(sess, "Model/model.ckpt")
tt_models(RL_prio, test_result)

# compare based on first success
# plt.plot(his_natural[0, :], his_natural[1, :] - his_natural[1, 0], c='b', label='natural DQN')
# plt.plot(his_prio[0, :], his_prio[1, :] - his_prio[1, 0], c='r', label='DQN with prioritized replay')
# plt.legend(loc='best')
# plt.ylabel('total training time')
# plt.xlabel('episode')
# plt.grid()
# plt.show()

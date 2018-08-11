import random
from collections import deque

import gym
import numpy as np
import tensorflow as tf
import gym_malware

# Hyper Parameters for DQN
GAMMA = 0.9  # discount factor for target Q
INITIAL_EPSILON = 0.5  # starting value of epsilon
FINAL_EPSILON = 0.01  # final value of epsilon
REPLAY_SIZE = 10000  # experience replay buffer size
BATCH_SIZE = 32  # size of minibatch


class DQN():
    # DQN Agent
    def __init__(self, env):  # 初始化
        # init experience replay
        self.replay_buffer = deque()
        # init some parameters
        self.time_step = 0
        self.epsilon = INITIAL_EPSILON
        self.state_dim = env.observation_space.shape[0]
        self.action_dim = env.action_space.n

        self.create_Q_network()
        self.create_training_method()

        # Init session
        self.session = tf.InteractiveSession()
        self.session.run(tf.global_variables_initializer())

        # loading networks
        self.saver = tf.train.Saver()
        checkpoint = tf.train.get_checkpoint_state("saved_networks")
        if checkpoint and checkpoint.model_checkpoint_path:
            self.saver.restore(self.session, checkpoint.model_checkpoint_path)
            print("Successfully loaded:", checkpoint.model_checkpoint_path)

        else:
            print("Could not find old network weights")

        global summary_writer
        summary_writer = tf.summary.FileWriter('logs', graph=self.session.graph)

    def create_Q_network(self):  # 创建Q网络
        # network weights
        W1 = self.weight_variable([self.state_dim, 20])
        b1 = self.bias_variable([20])
        W2 = self.weight_variable([20, self.action_dim])
        b2 = self.bias_variable([self.action_dim])
        # input layer
        self.state_input = tf.placeholder("float", [None, self.state_dim])
        # hidden layers
        h_layer = tf.nn.relu(tf.matmul(self.state_input, W1) + b1)
        # Q Value layer
        self.Q_value = tf.matmul(h_layer, W2) + b2

    def weight_variable(self, shape):
        initial = tf.truncated_normal(shape)
        return tf.Variable(initial)

    def bias_variable(self, shape):
        initial = tf.constant(0.01, shape=shape)
        return tf.Variable(initial)

    def create_training_method(self):  # 创建训练方法
        self.action_input = tf.placeholder("float", [None, self.action_dim])  # one hot presentation
        self.y_input = tf.placeholder("float", [None])
        Q_action = tf.reduce_sum(tf.multiply(self.Q_value, self.action_input), reduction_indices=1)
        self.cost = tf.reduce_mean(tf.square(self.y_input - Q_action))

        tf.summary.scalar("loss", self.cost)

        global merged_summary_op
        merged_summary_op = tf.summary.merge_all()

        self.optimizer = tf.train.AdamOptimizer(0.0001).minimize(self.cost)

    def perceive(self, state, action, reward, next_state, done):  # 感知存储信息
        one_hot_action = np.zeros(self.action_dim)
        one_hot_action[action] = 1
        self.replay_buffer.append((state, one_hot_action, reward, next_state, done))

        if len(self.replay_buffer) > REPLAY_SIZE:
            self.replay_buffer.popleft()

        if len(self.replay_buffer) > BATCH_SIZE:
            self.train_Q_network()

    def train_Q_network(self):  # 训练网络
        self.time_step += 1
        # Step 1: obtain random minibatch from replay memory
        minibatch = random.sample(self.replay_buffer, BATCH_SIZE)
        state_batch = [data[0] for data in minibatch]
        action_batch = [data[1] for data in minibatch]
        reward_batch = [data[2] for data in minibatch]
        next_state_batch = [data[3] for data in minibatch]

        # Step 2: calculate y
        y_batch = []
        Q_value_batch = self.Q_value.eval(feed_dict={self.state_input: next_state_batch})
        for i in range(0, BATCH_SIZE):
            done = minibatch[i][4]
            if done:
                y_batch.append(reward_batch[i])
            else:
                y_batch.append(reward_batch[i] + GAMMA * np.max(Q_value_batch[i]))

        self.optimizer.run(feed_dict={
            self.y_input: y_batch,
            self.action_input: action_batch,
            self.state_input: state_batch
        })

        summary_str = self.session.run(merged_summary_op, feed_dict={
            self.y_input: y_batch,
            self.action_input: action_batch,
            self.state_input: state_batch
        })
        summary_writer.add_summary(summary_str, self.time_step)

        # save network every 1000 iteration
        if self.time_step % 1000 == 0:
            self.saver.save(self.session, 'saved_networks/' + 'network' + '-dqn', global_step=self.time_step)

    def egreedy_action(self, state):  # 输出带随机的动作
        Q_value = self.Q_value.eval(feed_dict={
            self.state_input: [state]
        })[0]
        if random.random() <= self.epsilon:
            return random.randint(0, self.action_dim - 1)
        else:
            return np.argmax(Q_value)

        self.epsilon -= (INITIAL_EPSILON - FINAL_EPSILON) / 10000

    def action(self, state):  # 输出动作
        return np.argmax(self.Q_value.eval(feed_dict={
            self.state_input: [state]
        })[0])


# Hyper Parameters
ENV_NAME = 'malware-v0'
ENV_TEST_NAME = 'malware-test-v0'
EPISODE = 500  # Episode limitation
STEP = 80  # Step limitation in an episode
TEST = 1  # The number of experiment test every 10 episode
TEST_SAMPLE_COUNT = 200


def main():
    # initialize OpenAI Gym env and dqn agent
    env = gym.make(ENV_NAME)
    env_test = gym.make(ENV_TEST_NAME)
    agent = DQN(env)

    test_count = 0

    # Training...
    for episode in range(EPISODE):
        # initialize task
        state = env.reset()
        # Train
        for step in range(STEP):
            # e-greedy action for train
            action = agent.egreedy_action(state)
            next_state, reward, done, _ = env.step(action)
            agent.perceive(state, action, reward, next_state, done)
            state = next_state
            if done:
                break

        # 每1000次测试一下
        if episode % 10 == 0:
            # Testing...
            # ENV_TEST_NAME与ENV_NAME其实是一个env，区别在于读取samples的方法
            # 训练的时候是从1846-200=1646个样本中随机选取；测试的时候是从200个样本逐个读取
            for tt in range(TEST):
                test_count += 1
                total_reward = 0
                for i in range(TEST_SAMPLE_COUNT):
                    state = env_test.reset()
                    done = False
                    while not done:
                        # env.render()
                        action = agent.action(state)  # direct action for test
                        state, reward, done, _ = env_test.step(action)
                        # 规避成功reward是10，其他情况都是0，所以最后除以10可以统计，200个样本中规避成功了多少个文件
                        total_reward += reward

                ave_reward = total_reward / (TEST_SAMPLE_COUNT * 10)

                with open('NIS13DQN.txt', 'a+') as f:
                    f.write('episode:{} Evaluation Average Reward:{}\n'.format(test_count, ave_reward))
                    print('episode:{} Evaluation Average Reward:{}'.format(test_count, ave_reward))


if __name__ == '__main__':
    main()

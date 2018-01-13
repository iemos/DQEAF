# gym hello world
import gym

env = gym.make('CartPole-v0')
flag = 0
for i_episode in range(10):
    observation = env.reset()
    for t in range(100):
        env.render()
        # action either 0 or 1
        if flag == 0:
            action = 0
            flag = 1
        else:
            action = 1
            flag = 0
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            break

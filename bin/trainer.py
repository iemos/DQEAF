from train_agent_chainer import *

train_agent(rounds=5000, use_score=True, name='models/create_ddqn_agent_score_5000',
            create_agent=create_ddqn_agent)  # allow graduation_agent to see scores

train_agent(rounds=5000, use_score=False, name='models/create_ddqn_agent_5000',
            create_agent=create_ddqn_agent)  # black blox

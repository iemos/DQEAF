import bin.train_agent_chainer as tac

tac.train_agent(rounds=5000, use_score=True, name='models/create_ddqn_agent_score_5000',
                create_agent=tac.create_ddqn_agent)  # allow graduation_agent to see scores

tac.train_agent(rounds=5000, use_score=False, name='models/create_ddqn_agent_5000',
                create_agent=tac.create_ddqn_agent)  # black blox

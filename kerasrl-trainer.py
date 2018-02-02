import pickle

from bin.train_agent_kerasrl import train_dqn_model

agent1, model1, history_train1, history_test1 = train_dqn_model([1024, 256], rounds=50000, run_test=True,
                                                                use_score=False)  # black blox
model1.save('models/dqn.h5', overwrite=True)
with open('history_blackbox.pickle', 'wb') as f:
    pickle.dump(history_test1, f, pickle.HIGHEST_PROTOCOL)

agent2, model2, history_train2, history_test2 = train_dqn_model([1024, 256], rounds=50000, run_test=True,
                                                                use_score=True)  # allow graduation_agent to see scores
model2.save('models/dqn_score.h5', overwrite=True)
with open('history_score.pickle', 'wb') as f:
    pickle.dump(history_test2, f, pickle.HIGHEST_PROTOCOL)

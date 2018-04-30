from bin.test_agent_kerasrl import test_models

if __name__ == '__main__':
    result1, result2, result3 = test_models('bin/models/dqn.h5', '', False)
    print("{}, {}, {}\n".format(result1, result2, result3))

"""
Public test cases for the methods in agent.py
"""
import numpy as np

from agent import QLearningAgent


def test1():
    agent = QLearningAgent([4])
    agent.values.set_value([0], 0, 1)

    assert agent.get_greedy_action([0]) == 0, 'test 1 failed'
    print('test 1 passed!')


def test2():
    agent = QLearningAgent([4])
    agent.values.set_value([0], 0, 1)
    agent.values.set_value([0], 1, 1)

    count = np.zeros(4)
    num_samples = 100000
    for i in range(num_samples):
        a = agent.get_greedy_action([0])
        count[a] += 1

    print(count/num_samples)
    assert np.isclose(
        count/num_samples, np.array([1/2, 1/2, 0, 0]), atol=0.01).all(), 'test 2 failed'
    print('test 2 passed!')


def test3():
    agent = QLearningAgent([4])
    agent.values.set_value([0], 0, 1)
    count = np.zeros(4)
    num_samples = 1000000
    for i in range(num_samples):
        a = agent.get_action([0])
        count[a] += 1

    print(count/num_samples)

    assert np.isclose(
        count/num_samples, np.array([0.9 + 1/40, 1/40, 1/40, 1/40]), atol=0.001).all()
    print('test 3 passed!')


def test4():
    agent = QLearningAgent([4])
    agent.values.set_value([0], 0, 1)
    agent.values.set_value([0], 3, 1)
    count = np.zeros(4)
    num_samples = 1000000
    for i in range(num_samples):
        a = agent.get_action([0])
        count[a] += 1

    print(count/num_samples)

    assert np.isclose(
        count/num_samples, np.array([9/20+1/40, 1/40, 1/40, 9/20+1/40]), atol=0.001).all()
    print('test 4 passed!')


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()

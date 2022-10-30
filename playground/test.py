"""
Testing suite for perceptrons and neural networks.
Tests that changes to certain parts of the algoritms have the intended affects.
Tests that perceptrons and neural networks have expected accuracies
"""

import random
import unittest
import numpy
from perceptron_flexible import perceptron

#python -m unittest test.py -v

BIAS = 1
weights = [[random.random(), random.random(), random.random(), random.random(), \
    random.random(), random.random(), random.random()]]


def train(training_size, dynamic):
    '''Trains the perceptron weights'''
    _lr = 1
    trials = 25
    print('Initial Weights: ', weights)
    for _ in range(training_size):
        inputs = numpy.random.randint(2, size=6)
        output = ((inputs[0] or inputs[1]) and (inputs[2] and inputs[3])) \
            or (inputs[4] or inputs[5])
        perceptron(inputs, output, _lr)
        if dynamic:
            _lr -= (1/trials)

def run():
    '''Runs the perceptron on every input combination'''
    _lr = 0
    errors = 0
    for i in range(64):
        array = numpy.array([int(b) for b in format(i, '#08b')[2:]])
        out = ((array[0] or array[1]) and (array[2] and array[3])) or (array[4] or array[5])
        out_p = perceptron(array, out, _lr)
        if out != out_p:
            errors += 1
    return errors

def simulate(rounds, training_size, dynamic):
    '''Trains and runs the perceptron under certain conditions'''
    percent_success = numpy.array([])
    for _ in range(rounds):
        train(training_size, dynamic)
        _ps = (64-run())*100/64
        percent_success = numpy.append(percent_success, _ps)
    return numpy.mean(percent_success)



class TestPerceptron(unittest.TestCase):
    '''Runs a series of tests to ensure perceptron is functioning optimally'''

    def test_few_trials(self):
        '''Ensures accuracy > 80% for small training'''
        self.assertTrue(simulate(1000, 10, False) > 80)

    def test_decent_trials(self):
        '''Ensures accuracy > 85% for medium training'''
        self.assertTrue(simulate(1000, 25, False) > 85)

    def test_many_trials(self):
        '''Ensures accuracy > 90 for large training'''
        self.assertTrue(simulate(1000, 100, False) > 90)

    def test_dynamic(self):
        '''Ensures dynamic learning rate is more accurate'''
        non_dynamic = simulate(1000, 25, False)
        dynamic = simulate(1000, 25, True)
        self.assertTrue(dynamic > non_dynamic)

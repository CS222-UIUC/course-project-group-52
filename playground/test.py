import numpy
import perceptron_fun as pc
import unittest

def train(training_size, dynamic):
    lr = 1
    for i in range(training_size): 
        inputs = numpy.random.randint(2, size=6)
        output = ((inputs[0] or inputs[1]) and (inputs[2] and inputs[3])) or (inputs[4] or inputs[5])
        pc.Perceptron(inputs, output, lr)
        if dynamic: lr -= (1/training_size)

def run():
    errors = 0
    for i in range(64):
        array = numpy.array([int(b) for b in format(i, '#08b')[2:]])
        out = ((array[0] or array[1]) and (array[2] and array[3])) or (array[4] or array[5])
        outP = pc.Perceptron(array, out, 0)
        if (outP != out):
            errors += 1
    return errors

def simulate(rounds, training_size, dynamic):
    percent_success = numpy.array([])
    for i in range(rounds):
        train(training_size, dynamic)
        ps = (64-run())*100/64
        percent_success = numpy.append(percent_success, ps)
    return numpy.mean(percent_success)



class TestPerceptron(unittest.TestCase):

    def test_few_trials(self):
        self.assertTrue(simulate(1000, 10, False) > 80)

    def test_decent_trials(self):
        self.assertTrue(simulate(1000, 25, False) > 85)

    def test_many_trials(self):
        self.assertTrue(simulate(1000, 100, False) > 90)

    def test_dynamic(self):
        non_dynamic = simulate(1000, 25, False)
        dynamic = simulate(1000, 25, True)
        self.assertTrue(dynamic > non_dynamic)
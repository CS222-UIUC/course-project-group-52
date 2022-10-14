from audioop import bias
import numpy, random

class Perceptron:

    def __init__(self):
        self.bias = 1
        self.weights = [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random()]

    def activate(self, inputs, output, lr):
        outputP = numpy.sum(inputs*self.weights[:-1]) + self.bias*self.weights[-1]
        if outputP > 0:
            outputP = 1
        else:
            outputP = 0
        error = output - outputP
        self.weights[:-1] += error*inputs*lr
        self.weights[-1] += error*self.bias*lr

        return outputP
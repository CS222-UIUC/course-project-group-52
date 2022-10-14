import numpy, random


bias = 1
weights = [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random()]

def Perceptron(inputs, output, lr):
    global errors
    outputP = numpy.sum(inputs*weights[:-1]) + bias*weights[-1]
    if outputP > 0:
        outputP = 1
    else:
        outputP = 0
    error = output - outputP
    weights[:-1] += error*inputs*lr
    weights[-1] += error * bias * lr

    return outputP
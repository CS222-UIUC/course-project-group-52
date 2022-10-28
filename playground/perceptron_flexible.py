"""
Implementation of a perceptron algorithm.  Learns ((OR) AND (AND)) OR (OR)
Separate training and testing phases, customizable initial paramters
Perceptron is a function for easier expansion into full NN
"""

import numpy, random

def Perceptron(inputs, output):
    outputP = numpy.sum(inputs*weights[:-1]) + bias*weights[-1]
    if outputP > 0:
        outputP = 1
    else:
        outputP = 0
    error = output - outputP
    if error != 0:
        print('Input: ', inputs, '  Output: ', outputP, '    Expected: ', output)
        errors += 1
    weights[:-1] += error*inputs*lr
    weights[-1] += error * bias * lr

#initialize parameters of Perceptron, feel free to adjust
print('----------------[Start]----------------')
lr = 1 #learning rate - if set below 1, set dynamic to false (otherwise lr will become negative)
dynamic = True #does the learning rate decrease
bias = 1
weights = [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random()] #array is always size 7
trials = 25 #size of training set
print('Learning Rate:', lr, '   Dynamic: ', dynamic, '  Trials: ', trials, '\nBias: ', bias, '\nWeights: ', weights, '\n')
errors = 0 #don't change

#trains perceptron to emulate ((OR) AND (AND)) OR (OR)
print('----------------[Training]----------------')
print('Failures:')
for i in range(trials): 
    inputs = numpy.random.randint(2, size=6)
    output = ((inputs[0] or inputs[1]) and (inputs[2] and inputs[3])) or (inputs[4] or inputs[5])
    Perceptron(inputs, output)
    if dynamic: lr -= (1/trials)
print('\n')

#test on all possible inputs without learning
print('----------------[Testing]----------------')
print('Failurs:')
lr = 0
in1 = in2 = in3 = in4 = in5 = in6 = out = 0
errors = 0
for i in range(64):
    array = numpy.array([int(b) for b in format(i, '#08b')[2:]])
    out = ((array[0] or array[1]) and (array[2] and array[3])) or (array[4] or array[5])
    Perceptron(array, out)
print('\n')

print('----------------[Results]----------------')
print('Mistakes: ', errors)
print('Success Rate: ', (64-errors)*100/64, '%')
print('Final Weights: ', weights)
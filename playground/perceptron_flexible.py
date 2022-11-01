"""
Implementation of a perceptron algorithm.  Learns ((OR) AND (AND)) OR (OR)
Separate training and testing phases, customizable initial paramters
Perceptron is a function for easier expansion into full NN
"""

import random
import numpy

def perceptron(_inputs, _output, _lr):
    '''The activation of the perceptron, dot product of weights and imputs'''
    output_p = numpy.sum(_inputs*weights[:-1]) + BIAS*weights[-1]
    if output_p > 0:
        output_p = 1
    else:
        output_p = 0
    error = output - output_p
    if error != 0:
        print('Input: ', _inputs, '  Output: ', output_p, '    Expected: ', _output)
    weights[:-1] += error*_inputs*_lr
    weights[-1] += error * BIAS * _lr
    return output_p

#initialize parameters of Perceptron, feel free to adjust
print('----------------[Start]----------------')
LR = 1 #learning rate - if set below 1, set dynamic to false (otherwise lr will become negative)
DYNAMIC = True #does the learning rate decrease
BIAS = 1
weights = [random.random(), random.random(), random.random(), random.random(), \
     random.random(), random.random(), random.random()] #array is always size 7
TRIALS = 25 #size of training set
print('Learning Rate:', LR, '   Dynamic: ', DYNAMIC, '  Trials: ',\
     TRIALS, '\nBias: ', BIAS, '\nWeights: ', weights, '\n')

#trains perceptron to emulate ((OR) AND (AND)) OR (OR)
print('----------------[Training]----------------')
print('Failures:')
for i in range(TRIALS):
    inputs = numpy.random.randint(2, size=6)
    output = ((inputs[0] or inputs[1]) and (inputs[2] and inputs[3])) or (inputs[4] or inputs[5])
    perceptron(inputs, output, LR)
    if DYNAMIC:
        LR -= (1/TRIALS)
print('\n')

#test on all possible inputs without learning
print('----------------[Testing]----------------')
print('Failurs:')
LR = 0
ERRORS = 0
for i in range(64):
    array = numpy.array([int(b) for b in format(i, '#08b')[2:]])
    out = ((array[0] or array[1]) and (array[2] and array[3])) or (array[4] or array[5])
    out_p = perceptron(array, out, LR)
    if out_p != out:
        ERRORS += 1
print('\n')

print('----------------[Results]----------------')
print('Mistakes: ', ERRORS)
print('Success Rate: ', (64-ERRORS)*100/64, '%')
print('Final Weights: ', weights)

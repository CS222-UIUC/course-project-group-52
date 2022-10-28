'''
    This file expands the ideas in perceptron_flexible
    into a multilayer perceptron with 1 hidden layer
    consisting of 9 neurons
'''

import numpy as np

def relu(_x):
    '''takes an input x and returns x or 0, whichever is larger'''
    return np.max(0,_x)

def drelu(_x):
    '''the derivative of reLU (for backpropagation), return either 0 or 1'''
    return 1*(_x>0)

LR = 0.1
LAYER_SIZE = 9
INPUT_SIZE= 7 #6 inputs and a bias (defualt to 1 for now)
OUTPUT_SIZE = 1

hidden_weights = np.random.uniform(-1, 1, (INPUT_SIZE, LAYER_SIZE))
output_weights = np.random.uniform(-1, 1, LAYER_SIZE)

preActivation_H = np.zeros(LAYER_SIZE)
postActivation_H = np.zeros(LAYER_SIZE)

TRIALS = 25
for i in range(TRIALS):
    inputs = np.random.randint(2, size=6)
    inputs = np.append(inputs, 1) #bias
    output = ((inputs[0] or inputs[1]) and (inputs[2] and inputs[3])) or (inputs[4] or inputs[5])

    #feedforward
    for node in range(LAYER_SIZE):
        preActivation_H[node] = np.dot(inputs, hidden_weights[:,node])
        postActivation_H[node] = relu(preActivation_H[node])
    preActivation_O = np.dod(postActivation_H, output_weights)
    postActivation_O = relu(preActivation_O)

    error = postActivation_O - output

    #backpropogation
    
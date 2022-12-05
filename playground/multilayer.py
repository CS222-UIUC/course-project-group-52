'''
    This file expands the ideas in perceptron_flexible
    into a multilayer perceptron with 1 hidden layer
    consisting of 9 neurons
'''

import time
import csv
import numpy as np
from tensorflow import keras

def sigmoid(_x):
    '''Sigmoid activation function'''
    return 1 / (1+np.exp(-1*_x))

def dsigmoid(_x):
    '''Derivative of Sigmoid'''
    return sigmoid(_x) * (1 - sigmoid(_x))

def tanh(_x):
    '''Tanh activation function'''
    return np.tanh(_x)

def dtanh(_x):
    '''Derivative of Tanh'''
    return 1 - (np.tanh(_x)**2)

#hyperparameters, need adjustment
LR = 0.1
LAYER_SIZE = 20
INPUT_SIZE= 784
OUTPUT_SIZE = 10
EPOCHS = 10

hidden_weights = np.random.normal(loc=0, scale=1, size=(LAYER_SIZE, INPUT_SIZE))
output_weights = np.random.normal(loc=0, scale=1, size=(OUTPUT_SIZE, LAYER_SIZE))
hidden_bias = np.random.normal(loc=1, scale=1, size=(LAYER_SIZE))
output_bias = np.random.normal(loc=1, scale=1, size=(OUTPUT_SIZE))

with open('network.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow(np.zeros(10))
    writer.writerow(np.zeros(10))
    writer.writerow(np.zeros(OUTPUT_SIZE))
    writer.writerow(hidden_weights[:10,400:410].flatten())
    writer.writerow(output_weights[:,:10].flatten())

#runs the nn on the MNIST handwritten numbers dataset
#60,000 training arrays, 10,000 testing arrays, each array size 28 x 28 = 784
(train_inputs, train_outputs), (test_inputs, test_outputs) = keras.datasets.mnist.load_data()
mean = np.mean(train_inputs.flatten())
test_mean = np.mean(test_inputs.flatten())

st = time.time()
for e in range(EPOCHS):
    TRAIN_ERRORS = 0
    COUNT = 0
    for i in range(train_inputs.shape[0]):
        inputs = train_inputs[i].flatten()
        inputs = (inputs - mean) / 255
        outputs = np.zeros(OUTPUT_SIZE)
        outputs[train_outputs[i]] = 1

        hidden_act = tanh((hidden_weights @ inputs) + hidden_bias)
        output_act = sigmoid((output_weights @ hidden_act) + output_bias)
        error = (outputs - output_act)

        if np.argmax(output_act) != train_outputs[i]:
            TRAIN_ERRORS += 1

        bt = time.time()

        #derivative of output / hidden activation
        d_output = dsigmoid((output_weights @ hidden_act) + output_bias) * error
        d_hidden = dtanh((hidden_weights @ inputs) + hidden_bias) * (output_weights.T @ d_output)

        #derivative of cost with respect to output bias, output weights, hidden bias, hidden weights
        #reshape is same as transpose
        dc_db_o = -1*d_output
        dc_dw_o = (-1*hidden_act.reshape(LAYER_SIZE, 1) @ d_output.reshape(1, OUTPUT_SIZE)).T
        dc_dw_o = (-1*hidden_act.reshape(LAYER_SIZE, 1) @ d_output.reshape(1, OUTPUT_SIZE)).T
        dc_db_h = -1*d_hidden
        dc_dw_h = (-1 * inputs.reshape(INPUT_SIZE, 1) @ d_hidden.reshape(LAYER_SIZE, 1).T).T

        output_bias -= LR * dc_db_o
        output_weights -= LR * dc_dw_o
        hidden_bias -= LR * dc_db_h
        hidden_weights -= LR * dc_dw_h

        if COUNT % 1000 == 0:
            with open('network.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file, lineterminator='\n')
                writer.writerow(inputs[400:410])
                writer.writerow(hidden_act[:10])
                writer.writerow(output_act)
                writer.writerow(hidden_weights[:10,400:410].flatten())
                writer.writerow(output_weights[:,:10].flatten())
        COUNT += 1

    print('Epoch: ',e+1,'/',EPOCHS,'\tAccuracy: ',round((60000-TRAIN_ERRORS)/600, 3),'%',end='\r')

ERRORS = 0
COUNT = 0
for i in range(test_inputs.shape[0]):
    inputs = test_inputs[i].flatten()
    inputs = (inputs - test_mean)/255

    hidden_act = tanh((hidden_weights @ inputs) + hidden_bias)
    output_act = sigmoid((output_weights @ hidden_act) + output_bias)

    if np.argmax(output_act) != test_outputs[i]:
        ERRORS += 1

    if COUNT % 1000 == 0:
        with open('network.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(inputs[400:410])
            writer.writerow(hidden_act[:10])
            writer.writerow(output_act)
            writer.writerow(hidden_weights[:10,400:410].flatten())
            writer.writerow(output_weights[:,:10].flatten())
    COUNT += 1

et = time.time()

print('\n----------------[Results]----------------')
print('Mistakes: ', ERRORS)
print('Success Rate: ', (test_inputs.shape[0]-ERRORS)*100/test_inputs.shape[0], '%')
print('Time: ', round((et-st)/60,3), 'minutes')

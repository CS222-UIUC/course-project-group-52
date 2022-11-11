'''
    This file expands the ideas in perceptron_flexible
    into a multilayer perceptron with 1 hidden layer
    consisting of 9 neurons
'''

import numpy as np
from tensorflow import keras

def sigmoid(_x):
    '''top is relu, bottom is sigmoid'''
    return max(0,_x)
    # return 1/(1+np.exp(-_x))

def dsigmoid(_x):
    '''the derivative of relu(top) and sigmoid (bottom)'''
    return 1*(_x>0)
    # return sigmoid(_x)*(1-sigmoid(_x))

LR = 0.1
LAYER_SIZE = 5
INPUT_SIZE= 784 #does not include bais
OUTPUT_SIZE = 1
TRIALS = 150

hidden_weights = np.random.uniform(-1, 1, (INPUT_SIZE+1, LAYER_SIZE))
output_weights = np.random.uniform(-1, 1, LAYER_SIZE+1)

preActivation_H = np.zeros(LAYER_SIZE+1)
preActivation_H[-1] = 1 #bias
postActivation_H = np.zeros(LAYER_SIZE+1)

#----------------[Training]----------------
def train(_inputs, _output):
    '''trains the network on an array of inputs and an output'''

    #feedforward
    for node in range(LAYER_SIZE):
        preActivation_H[node] = np.dot(_inputs, hidden_weights[:,node])
        postActivation_H[node] = sigmoid(preActivation_H[node])
    pre_activation_o = np.dot(postActivation_H, output_weights)
    post_activation_o = sigmoid(pre_activation_o)

    error = post_activation_o - _output

    #backpropogation
    for hidden_node in range(LAYER_SIZE):
        s_error = error * dsigmoid(pre_activation_o)
        gradient_output = s_error * postActivation_H[hidden_node]

        for input_node in range(INPUT_SIZE):
            gradient_hidden = s_error * output_weights[hidden_node] * \
                dsigmoid(preActivation_H[hidden_node]) * _inputs[input_node]
            hidden_weights[input_node, hidden_node] -= LR * gradient_hidden

        output_weights[hidden_node] -= LR * gradient_output

    # LR = LR*(1-0.01)**i
#----------------[Testing]----------------
def test(_inputs):
    '''runs the network on an array of inputs'''

    for node in range(LAYER_SIZE):
        preActivation_H[node] = np.dot(_inputs, hidden_weights[:,node])
        postActivation_H[node] = sigmoid(preActivation_H[node])
    pre_activation_o = np.dot(postActivation_H, output_weights)
    post_activation_o = sigmoid(pre_activation_o)

    return post_activation_o

#runs the nn on the MNIST handwritten numbers dataset
#60,000 training arrays, 10,000 testing arrays, each array size 28 x 28 = 784
(train_inputs, train_outputs), (test_inputs, test_outputs) = keras.datasets.mnist.load_data()
for i in range(train_inputs.shape[0]):
    inputs = train_inputs[i].flatten()
    inputs = np.append(inputs, 1) #append bias
    train(inputs, train_outputs[i])

ERRORS = 0
for i in range(test_inputs.shape[0]):
    inputs = test_inputs[i].flatten()
    inputs = np.append(inputs, 1)
    out = test(inputs)
    if out != test_outputs[i]:
        ERRORS += 1

print('----------------[Results]----------------')
print('Mistakes: ', ERRORS)
print('Success Rate: ', (test_inputs.shape[0]-ERRORS)*100/test_inputs.shape[0], '%')

'''
    This file expands the ideas in perceptron_flexible
    into a multilayer perceptron with 1 hidden layer
    consisting of 9 neurons
'''

import time
import numpy as np
from tensorflow import keras

def relu(_x):
    '''top is relu, bottom is sigmoid'''
    return max(0,_x)
    # return 1/(1+np.exp(-_x))

def drelu(_x):
    '''the derivative of relu(top) and sigmoid (bottom)'''
    return 1*(_x>0)
    # return sigmoid(_x)*(1-sigmoid(_x))

LR = 0.1
LAYER_SIZE = 5
INPUT_SIZE= 784
OUTPUT_SIZE = 10
TRIALS = 150
EPOCHS = 1
BATCH_SIZE = 100

hidden_weights = np.random.uniform(-1.0, 1.0, (LAYER_SIZE, INPUT_SIZE))
output_weights = np.random.uniform(-1.0, 1.0, (OUTPUT_SIZE, LAYER_SIZE))
hidden_bias = np.zeros(LAYER_SIZE, dtype=float)
output_bias = np.zeros(OUTPUT_SIZE, dtype=float)
hidden_act = np.zeros(LAYER_SIZE, dtype=float)
output_act = np.zeros(OUTPUT_SIZE, dtype=float)

#----------------[Training]----------------
def forward(_inputs):
    '''forward propagation'''

    #feedforward
    for node in range(LAYER_SIZE):
        hidden_act[node] += relu(np.dot(_inputs, hidden_weights[node])+hidden_bias[node])

    for node in range(OUTPUT_SIZE):
        output_act[node] += relu(np.dot(hidden_act, output_weights[node])+output_bias[node])

    # cost = np.sum((output_act - _output)**2)

    #backpropogation
def back(_inputs, _output):
    '''backpropagation'''
    a = hidden_bias
    for output_node in range(OUTPUT_SIZE):
        dc_db_o = drelu(np.dot(hidden_act, output_weights[output_node])+output_bias[output_node])*2*(output_act[output_node] - _output[output_node])
        #derivative of cost of output with respect to bias
        dc_dw_o = hidden_act*dc_db_o
        #derivative of cost of output with respect to weight

        output_bias[output_node] -= LR * dc_db_o
        output_weights[output_node] -= LR * dc_dw_o

        #same as above, but for previous layer
        for hidden_node in range(LAYER_SIZE):
            dc_db_h = drelu(np.dot(_inputs, hidden_weights[hidden_node])+hidden_bias[hidden_node])*2*(output_act[output_node] - _output[output_node])
            dc_dw_h = _inputs*dc_db_h

            # a = hidden_weights[hidden_node]
            print(hidden_bias[hidden_node].shape)
            print((LR * dc_db_h).shape)
            hidden_bias[hidden_node] -= LR * dc_db_h
            print(hidden_bias[hidden_node] - (hidden_bias[hidden_node] - (LR * dc_db_h)))
            hidden_weights[hidden_node,:] -= LR * dc_dw_h
            # b = hidden_weights[hidden_node]
            # if ((LR * dc_dw_h)[74] != 0):
            #     print(hidden_weights[hidden_node])
            #     print(dc_dw_h * LR)
            #     print(hidden_weights[hidden_node] - LR * dc_dw_h)
            # print(a-b)
    print(a - hidden_bias)



    # for hidden_node in range(LAYER_SIZE):
    #     s_error = error * drelu(pre_activation_o)
    #     gradient_output = s_error * postActivation_H[hidden_node]

    #     for input_node in range(INPUT_SIZE):
    #         gradient_hidden = s_error * output_weights[hidden_node] * \
    #             drelu(preActivation_H[hidden_node]) * _inputs[input_node]
    #         hidden_weights[input_node, hidden_node] -= LR * gradient_hidden

    #     output_weights[hidden_node] -= LR * gradient_output

    # LR = LR*(1-0.01)**i
#----------------[Testing]----------------
# def test(_inputs):
#     '''runs the network on an array of inputs'''

#     for node in range(LAYER_SIZE):
#         preActivation_H[node] = np.dot(_inputs, hidden_weights[:,node])
#         postActivation_H[node] = relu(preActivation_H[node])
#     pre_activation_o = np.dot(postActivation_H, output_weights)
#     post_activation_o = relu(pre_activation_o)

#     return post_activation_o

#runs the nn on the MNIST handwritten numbers dataset
#60,000 training arrays, 10,000 testing arrays, each array size 28 x 28 = 784
(train_inputs, train_outputs), (test_inputs, test_outputs) = keras.datasets.mnist.load_data()

st = time.time()
# a = hidden_weights[0]
for e in range(EPOCHS):
    # print(hidden_weights[0])
    COUNTER = 1
    CURRENT_BATCH = 0
    # print(hidden_weights)
    average_inputs = np.zeros(INPUT_SIZE, dtype=float)
    average_outputs = np.zeros(OUTPUT_SIZE, dtype=float)
    for i in range(train_inputs.shape[0]):
        inputs = train_inputs[i].flatten()
        average_inputs += inputs
        outputs = np.zeros(OUTPUT_SIZE, dtype=float)
        outputs[train_outputs[i]] = 1
        average_outputs += train_outputs[i]
        forward(inputs)
        CURRENT_BATCH += 1

        if CURRENT_BATCH == BATCH_SIZE:
            bt = time.time()
            # print("Epoch: ",e+1,'/',EPOCHS,"\tBatch: ",COUNTER,'/',int(60000/BATCH_SIZE),"\tTime: ",round((bt-st)/60,3), end='\r')
            average_inputs /= BATCH_SIZE
            average_outputs /= BATCH_SIZE
            # print(average_inputs)
            hidden_act /= BATCH_SIZE
            output_act /= BATCH_SIZE
            back(average_inputs, average_outputs)
            hidden_act = np.zeros(LAYER_SIZE, dtype=float)
            output_act = np.zeros(OUTPUT_SIZE, dtype=float)
            average_inputs = np.zeros(INPUT_SIZE, dtype=float)
            average_outputs = np.zeros(OUTPUT_SIZE, dtype=float)
            CURRENT_BATCH = 0
            COUNTER += 1

# b = hidden_weights[0]
# print(a-b)
ERRORS = 0
for i in range(test_inputs.shape[0]):
    inputs = test_inputs[i].flatten()
    hidden_act = np.zeros(LAYER_SIZE)
    output_act = np.zeros(OUTPUT_SIZE)
    forward(inputs)
    if np.max(np.abs(output_act)) != test_outputs[i]:
        ERRORS += 1

et = time.time()

print('\n----------------[Results]----------------')
print('Mistakes: ', ERRORS)
print('Success Rate: ', (test_inputs.shape[0]-ERRORS)*100/test_inputs.shape[0], '%')
print('Time: ', round((et-st)/60,3), 'minutes')

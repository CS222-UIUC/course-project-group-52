'''
    This file expands the ideas in perceptron_flexible
    into a multilayer perceptron with 1 hidden layer
    consisting of 9 neurons
'''

import time
import numpy as np
from tensorflow import keras

def sigmoid(_x):
    return 1 / (1+np.exp(-1*_x))

def dsigmoid(_x):
    return sigmoid(_x) * (1 - sigmoid(_x))

def tanh(_x):
    return np.tanh(_x)

def dtanh(_x):
    return 1 - (np.tanh(_x)**2)

def relu(_x):
    '''top is relu, bottom is sigmoid'''
    return np.maximum(0,_x)
    # return 1/(1+np.exp(-_x))

def drelu(_x):
    '''the derivative of relu(top) and sigmoid (bottom)'''
    return 1*(_x>0)
    # return relu(_x)*(1-relu(_x))

def test_drelu(_x):
    _x[_x<=0] = 0
    _x[_x>0] = 1
    return _x

LR = 0.1
LAYER_SIZE = 75
INPUT_SIZE= 784
OUTPUT_SIZE = 10
TRIALS = 150
EPOCHS = 1
BATCH_SIZE = 1

hidden_weights = np.random.uniform(-1, 1, (LAYER_SIZE, INPUT_SIZE))
output_weights = np.random.uniform(-1, 1, (OUTPUT_SIZE, LAYER_SIZE))
hidden_bias = np.random.uniform(-1, 1, LAYER_SIZE)
output_bias = np.random.uniform(-1, 1, OUTPUT_SIZE)
hidden_act = np.zeros(LAYER_SIZE)
output_act = np.zeros(OUTPUT_SIZE)

#----------------[Training]----------------
# def forward(_inputs):
#     '''forward propagation'''

#     #feedforward
#     for node in range(LAYER_SIZE):
#         hidden_act[node] += relu(np.dot(_inputs, hidden_weights[node])+hidden_bias[node])

#     for node in range(OUTPUT_SIZE):
#         output_act[node] += relu(np.dot(hidden_act, output_weights[node])+output_bias[node])

#     # cost = np.sum((output_act - _output)**2)

#     #backpropogation
# def back(_inputs, _output):
#     '''backpropagation'''
#     for output_node in range(OUTPUT_SIZE):
#         dc_db_o = drelu(np.dot(hidden_act, output_weights[output_node])+output_bias[output_node])*2*(output_act[output_node] - _output[output_node])
#         #derivative of cost of output with respect to bias
#         dc_dw_o = hidden_act*dc_db_o
#         #derivative of cost of output with respect to weight

#         output_bias[output_node] -= LR * dc_db_o
#         output_weights[output_node] -= LR * dc_dw_o

#         #same as above, but for previous layer
#         for hidden_node in range(LAYER_SIZE):
#             dc_db_h = drelu(np.dot(_inputs, hidden_weights[hidden_node])+hidden_bias[hidden_node])*2*(output_act[output_node] - _output[output_node])
#             dc_dw_h = _inputs*dc_db_h

#             hidden_bias[hidden_node] -= LR * dc_db_h
#             hidden_weights[hidden_node] -= LR * dc_dw_h



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
mean = np.mean(train_inputs.flatten())

# a = hidden_bias
# print(hidden_bias)
# hidden_bias += 5
# print(hidden_bias)
st = time.time()
for e in range(EPOCHS):
    # print()
    # print(output_bias)
    # print()
    # hidden_bias[0] += 5
    COUNTER = 1
    CURRENT_BATCH = 0
    average_inputs = np.zeros(INPUT_SIZE)
    average_outputs = np.zeros(OUTPUT_SIZE)
    for i in range(train_inputs.shape[0]):
    # for i in range(1):
        inputs = train_inputs[i].flatten()
        # inputs = (inputs - mean) / 255
        average_inputs += inputs
        outputs = np.zeros(OUTPUT_SIZE)
        outputs[train_outputs[i]] = 1
        average_outputs += outputs
        # forward(inputs)

        #used to be function fdorward
        act_h = tanh((hidden_weights @ inputs) + hidden_bias)
        act_o = sigmoid((output_weights @ act_h) + output_bias)
        hidden_act += act_h
        output_act += act_o
        # for node in range(LAYER_SIZE):
        #     print(np.dot(inputs, hidden_weights[node])+hidden_bias[node])
        #     hidden_act[node] += relu(np.dot(inputs, hidden_weights[node])+hidden_bias[node])
        # for node in range(OUTPUT_SIZE):
        #     # print(output_weights[node])
        #     # print(np.dot(hidden_act, output_weights[node]))
        #     output_act[node] += relu(np.dot(hidden_act, output_weights[node])+output_bias[node])
        #end of function

        CURRENT_BATCH += 1
        if CURRENT_BATCH == BATCH_SIZE:
            bt = time.time()
            print("Epoch:",e+1,'/',EPOCHS," \tBatch:",COUNTER,'/',int(60000/BATCH_SIZE)," \t\tTime:",round((bt-st)/60,3), end='\r')
            average_inputs /= BATCH_SIZE
            average_outputs /= BATCH_SIZE
            hidden_act /= BATCH_SIZE
            output_act /= BATCH_SIZE
            # back(average_inputs, average_outputs)
            # print()
            # print(output_bias[0])
            # print()
            #used to be function back
            #reshape is same as transpose
            error = (output_act - average_outputs)
            # print(output_act)
            # print(average_outputs)
            # print(error)
            z_o = dsigmoid((output_weights @ hidden_act) + output_bias) * error
            z_h = dtanh((hidden_weights @ average_inputs) + hidden_bias) * (output_weights.T @ z_o)
            dc_db_o = -1*z_o
            dc_dw_o = (-1*hidden_act.reshape(LAYER_SIZE, 1) @ z_o.reshape(1, OUTPUT_SIZE)).T
            dc_db_h = -1*z_h
            dc_dw_h = (-1 * average_inputs.reshape(INPUT_SIZE, 1) @ z_h.reshape(LAYER_SIZE, 1).T).T

            output_bias -= LR * dc_db_o
            output_weights -= LR * dc_dw_o
            hidden_bias -= LR * dc_db_h
            hidden_weights -= LR * dc_dw_h

            # for output_node in range(OUTPUT_SIZE):
            #     dc_db_o = drelu(np.dot(hidden_act, output_weights[output_node])+output_bias[output_node])*2*(output_act[output_node] - average_outputs[output_node])
            #     #derivative of cost of output with respect to bias
            #     # print(dc_db_o.size)
            #     # print(hidden_act.size)
            #     dc_dw_o = hidden_act*dc_db_o
            #     #derivative of cost of output with respect to weight

            #     output_bias[output_node] -= LR * dc_db_o
            #     output_weights[output_node] -= LR * dc_dw_o

            #     #same as above, but for previous layer
            #     for hidden_node in range(LAYER_SIZE):
            #         dc_db_h = drelu(np.dot(average_inputs, hidden_weights[hidden_node])+hidden_bias[hidden_node])*2*(output_act[output_node] - average_outputs[output_node])/BATCH_SIZE
            #         dc_dw_h = average_inputs*dc_db_h

            #         hidden_bias[hidden_node] -= LR * dc_db_h
            #         hidden_weights[hidden_node] -= LR * dc_dw_h
            # #end of function


            hidden_act = np.zeros(LAYER_SIZE)
            output_act = np.zeros(OUTPUT_SIZE)
            average_inputs = np.zeros(INPUT_SIZE)
            average_outputs = np.zeros(OUTPUT_SIZE)
            CURRENT_BATCH = 0
            COUNTER += 1

ERRORS = 0
for i in range(test_inputs.shape[0]):
    inputs = test_inputs[i].flatten()
    # inputs = (inputs - mean)/255
    # hidden_act = np.zeros(LAYER_SIZE)
    # output_act = np.zeros(OUTPUT_SIZE)
    # forward(inputs)

    #function forward
    hidden_act = tanh((hidden_weights @ inputs) + hidden_bias)
    output_act = sigmoid((output_weights @ hidden_act) + output_bias)
    # for node in range(LAYER_SIZE):
    #     hidden_act[node] += relu(np.dot(inputs, hidden_weights[node])+hidden_bias[node])
    # for node in range(OUTPUT_SIZE):
    #     output_act[node] += relu(np.dot(hidden_act, output_weights[node])+output_bias[node])
    #end of fucntion

    if np.argmax(output_act) != test_outputs[i]:
        ERRORS += 1

et = time.time()

# print(hidden_bias)
# print(hidden_bias - a)

print('\n----------------[Results]----------------')
# print(output_bias)
print('Mistakes: ', ERRORS)
print('Success Rate: ', (test_inputs.shape[0]-ERRORS)*100/test_inputs.shape[0], '%')
print('Time: ', round((et-st)/60,3), 'minutes')

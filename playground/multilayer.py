'''
    This file expands the ideas in perceptron_flexible
    into a multilayer perceptron with 1 hidden layer
    consisting of 9 neurons
'''

import numpy as np

def relu(_x):
    '''takes an input x and returns x or 0, whichever is larger'''
    return max(0,_x)

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

#----------------[Training]----------------
TRIALS = 25
for i in range(TRIALS):
    inputs = np.random.randint(2, size=INPUT_SIZE-1)
    inputs = np.append(inputs, 1) #bias
    output = ((inputs[0] or inputs[1]) and (inputs[2] and inputs[3])) or (inputs[4] or inputs[5])

    #feedforward
    for node in range(LAYER_SIZE):
        preActivation_H[node] = np.dot(inputs, hidden_weights[:,node])
        postActivation_H[node] = relu(preActivation_H[node])
    preActivation_O = np.dot(postActivation_H, output_weights)
    postActivation_O = relu(preActivation_O)

    error = postActivation_O - output

    #backpropogation
    for hidden_node in range(LAYER_SIZE):
        S_error = error * drelu(preActivation_O)
        gradient_output = S_error * postActivation_H[hidden_node]

        for input_node in range(INPUT_SIZE):
            gradient_hidden = S_error * output_weights[hidden_node] * drelu(preActivation_H[hidden_node]) * inputs[input_node]
            hidden_weights[input_node, hidden_node] -= LR * gradient_hidden
        
        output_weights[hidden_node] -= LR * gradient_output

    LR = LR*(1-0.01)**i
#----------------[Testing]----------------
ERRORS = 0
for i in range(64):
    array = np.array([int(b) for b in format(i, '#08b')[2:]])
    array = np.append(array, 1)
    out = ((array[0] or array[1]) and (array[2] and array[3])) or (array[4] or array[5])
    for node in range(LAYER_SIZE):
        preActivation_H[node] = np.dot(array, hidden_weights[:,node])
        postActivation_H[node] = relu(preActivation_H[node])
    preActivation_O = np.dot(postActivation_H, output_weights)
    postActivation_O = relu(preActivation_O)

    if np.abs(postActivation_O) > 0.5:
        OUTPUT = 1
    else:
        OUTPUT = 0

    if OUTPUT != out:
        print(preActivation_O, ' ' , postActivation_O, ' ', OUTPUT, out)
        ERRORS += 1

print('----------------[Results]----------------')
print('Mistakes: ', ERRORS)
print('Success Rate: ', (64-ERRORS)*100/64, '%')

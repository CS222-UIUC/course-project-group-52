"""
Implementation of the Perceptron algorithm. Learns the  boolean OR function
"""

import random

def dot_product(_m1, _m2):
    """ We will use this to multiply input and weight vectors"""
    product = sum(_m1[i] * _m2[i] for i in range(len(_m1)))
    return product

def sgn_activation(_w, _x):
    """ Returns 1/0 based on dot product"""
    _wx = dot_product(_w, _x)
    if _wx > 0:
        return 1
    return 0

#                          --- Initialisation ---

# Input array with format [input1, input2] for OR function
X = [
[0, 0],
[0, 1],
[1, 0],
[1, 1],
]

# Target outputs
targets = [0, 1, 1, 1]

# Initialising each weight such that -1 < w < 1
# W_ij where i = input value; j = input dimension
# weights = [[round(random.uniform(-1, 1), 3),
#             round(random.uniform(-1, 1), 3)] for item in X]

weights = [round(random.uniform(-1, 1), 3),round(random.uniform(-1, 1), 3)]

# Training

ITERATIONS = 0
LEARNING_RATE = 0.25
NOT_ACCURATE = True
M = len(X)
while ITERATIONS <= 10:
    ITERATIONS += 1
    CORRECTS = 0
    # Looping through each pair of weights and inputs
    for i in range(M):
        Y = sgn_activation(X[i], weights)
        t = targets[i]
        if Y == t:
            CORRECTS += 1
        else:
            diff = Y - t
            for n in range(2):
                # Updating weights based on difference between target and actual output
                weights[n] -= LEARNING_RATE * diff * X[i][n]
        print('\n',ITERATIONS)
        print('Current Weights: ', weights)
        print('Current Activations: ', [sgn_activation(weights, X[i]) for i in range(M)])

    if ITERATIONS == 10:
        # Recall
        print('\n• Final Weights: ', weights)
        print('• Iterations: ', ITERATIONS)
        print('• Final Activations: ',[sgn_activation(weights, X[i]) for i in range(M)])
        NOT_ACCURATE = False
    else:
        continue

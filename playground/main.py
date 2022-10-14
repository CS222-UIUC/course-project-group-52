import numpy, random
import perceptron_fun as pc

'''----------------[Start]----------------'''
p = pc.Perceptron()
lr = 1
dynamic = True
trials = 25
print('Initial Weights: ', p.weights)

'''----------------[Training]----------------'''
for _ in range(trials):
    inputs = numpy.random.randint(2, size=6)
    output = ((inputs[0] or inputs[1]) and (inputs[2] and inputs[3])) or (inputs[4] or inputs[5])
    p.activate(inputs, output, lr)
    if dynamic: lr -= (1/trials)
print ('-----------------------------------------')
'''----------------[Testing]----------------'''
lr = 0
errors = 0
for i in range(64):
    array = numpy.array([int(b) for b in format(i, '#08b')[2:]])
    out = ((array[0] or array[1]) and (array[2] and array[3])) or (array[4] or array[5])
    out = p.activate(array, out, lr)
    if (out != output):
            errors += 1

'''----------------[Results]----------------'''
print('Mistakes: ', errors)
print('Success Rate: ', (64-errors)*100/64, '%')
print('Final Weights: ', p.weights)
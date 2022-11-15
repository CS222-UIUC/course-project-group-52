import numpy as np


LR = 0.1
LAYER_SIZE = 5
INPUT_SIZE= 5
OUTPUT_SIZE = 5
TRIALS = 150
EPOCHS = 1
BATCH_SIZE = 100

hidden_weights = np.random.uniform(-1.0, 1.0, (LAYER_SIZE, INPUT_SIZE))
output_weights = np.random.uniform(-1.0, 1.0, (OUTPUT_SIZE, LAYER_SIZE))
hidden_bias = np.zeros(LAYER_SIZE, dtype=float)
output_bias = np.zeros(OUTPUT_SIZE, dtype=float)
hidden_act = np.zeros(LAYER_SIZE, dtype=float)
output_act = np.zeros(OUTPUT_SIZE, dtype=float)
inputs = np.zeros(INPUT_SIZE, dtype=float)
inputs[3] = 6

print(hidden_weights)
# hidden_weights[0] -= inputs
def add():
    for i in range(5):
        hidden_weights[i] -= LR * inputs
add()
print(hidden_weights)

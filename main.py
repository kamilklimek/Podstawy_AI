        #add activation functions
import NeuralNetwork as nn
from ActivationFunctions import Activation


layer_2_linear = nn.NeuralNetwork([2, 2, 1], "LINEAR")
layer_1_linear = nn.NeuralNetwork([2, 1], "LINEAR")

layer_2_sig = nn.NeuralNetwork([2, 2, 1], "SIGM")
layer_1_sig = nn.NeuralNetwork([2, 1], "SIGM")

layer_2_binary = nn.NeuralNetwork([2, 2, 1], "BINARY_STEP")
layer_1_binary = nn.NeuralNetwork([2, 1], "BINARY_STEP")

print(layer_2_linear)
print(layer_1_linear)

print("[1] Layer - Linear " + str(layer_1_linear.feed_forward([[1, 1]])))
print("[2] Layer - Linear " + str(layer_2_linear.feed_forward([[1, 1]])))


print("[1] Layer - Sigm " + str(layer_1_sig.feed_forward([[1, 1]])))
print("[2] Layer - Sigm " + str(layer_2_sig.feed_forward([[1, 1]])))


print("[1] Layer - Binary Step " + str(layer_1_binary.feed_forward([[-1, 1]])))
print("[2] Layer - Binary Step " + str(layer_2_binary.feed_forward([[-1, 1]])))
        #add activation functions
import NeuralNetwork as nn


layer_2_linear = nn.NeuralNetwork([2, 2, 1], "LINEAR")
layer_1_linear = nn.NeuralNetwork([2, 1], "LINEAR")

print("[2] Layer - Linear " + str(layer_2_linear.feed_forward([[1, 1]])))
print("[1] Layer - Linear " + str(layer_1_linear.feed_forward([[1, 1]])))
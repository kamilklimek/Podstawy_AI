        #add activation functions
import NeuralNetwork as nn


layer_2_linear = nn.NeuralNetwork([[2, 1]], "LINEAR")
layer_2_sigm = nn.NeuralNetwork([2, 1])
layer_2_binary_step = nn.NeuralNetwork([2, 1], "BINARY_STEP")

layer_1_linear =nn.NeuralNetwork([[2, 1]], "LINEAR")
layer_1_sigm = nn.NeuralNetwork([[2, 1]], "SIGM")
layer_1_binary_step =nn.NeuralNetwork([[2, 1]], "BINARY_STEP")

print("[2] Layer - Linear " + str(layer_2_linear.feed_forward([[1, 1]])))
print("[2] Layer - Sigm " + str(layer_2_sigm.feed_forward([[1, 1]])))
print("[2] Layer - Binary step " + str(layer_2_binary_step.feed_forward([[1, 1]])))
print("[1] Layer - Linear " + str(layer_1_linear.feed_forward([[1, 1]])))
print("[1] Layer - Sigm " + str(layer_1_sigm.feed_forward([[1, 1]])))
print("[1] Layer - Binary Step " + str(layer_1_binary_step.feed_forward([[1, 1]])))
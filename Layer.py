import MatrixOperations as mx
import random
import numpy as np
import ActivationFunctions as func


class Layer:
    def __init__(self, height, input_size, activation="SIGM"):
        self.weights = np.random.rand(height, input_size)
        self.biases = np.random.rand(height, 1)
        self.activation = activation
        
    def get_biases(self):
        return self.biases


    def get_weights(self):
        return self.weights

    def sigm(self, output):
        for i in range(len(output)):
            for j in range(len(output[i])):
                output[i][j] = func.sigmoid(output[i][j])
        return output


    def linear(self, output):
        for i in range(len(output)):
            for j in range(len(output[i])):
                output[i][j] = func.linear(output[i][j])

        return output

    def binary_step(self, output):
        for i in range(len(output)):
            for j in range(len(output[i])):
                output[i][j] = func.binary_step(output[i][j])

        return output


    def activ(self, output):
        activation = self.activation

        if activation == "SIGM":
            return self.sigm(output)
        elif activation == "LINEAR":
            return self.linear(output)
        elif activation == "BINARY_STEP":
            return self.binary_step(output)



    def feed_forward(self, inputs: list):
        multiply_result = mx.multiply(self.weights, inputs)
        output = mx.add_matrix(multiply_result, self.biases)
        return self.activ(output)

    def __str__(self):
        return "weights: " + str(self.weights) + ", biases: " + str(self.biases);


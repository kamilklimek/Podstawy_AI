import MatrixOperations as mx
import random
import numpy as np
import ActivationFunctions as func
import RandomMatrix


class Layer:
    def __init__(self, number_of_weights, number_of_nodes, activation="SIGM"):
        self.weights = RandomMatrix.get_random_matrix(number_of_weights, number_of_nodes)
        #self.weights = mx.reshape(self.weights, number_of_weights, number_of_nodes)
        self.biases = RandomMatrix.get_random_matrix(1, number_of_nodes)
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
        print("====================================")
        print("Otrzymuje input: " + str(inputs))
        print("Moje wagi: " + str(self.weights))
        print("Mój bias: " + str(self.biases))
        multiply_result = mx.multiply(inputs, self.weights)
        output = mx.add_matrix(multiply_result, self.biases)
        print("Output przed aktywacja: " + str(output))
        input("Type enter...")
        return self.activ(output)

    def __str__(self):
        return "weights: " + str(self.weights) + ", biases: " + str(self.biases);


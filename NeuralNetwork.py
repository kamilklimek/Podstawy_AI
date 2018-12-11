import Layer


class NeuralNetwork:
    def __init__(self, archetype, activation = "SIGM"):
        self.layers = []
        for i in range(0, len(archetype)-1):
            number_of_weights = archetype[i]
            number_of_nodes = archetype[i+1]
            l = Layer.Layer(number_of_weights, number_of_nodes, activation)
            self.layers.append(l)
            

    def feed_forward(self, inputs: list):
        output = inputs.copy()
        layer_nr = 1
        for layer in self.layers:
            print("Layer numer: " + str(layer_nr))
            layer_nr+=1
            output = layer.feed_forward(output)
        return output

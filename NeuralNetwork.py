import Layer


class NeuralNetwork:
    def __init__(self, archetype, activation = "SIGM"):
        self.layers = []
        for i in range(1, len(archetype)):
            l = Layer.Layer(archetype[i - 1], archetype[i], activation)
            self.layers.append(l)
            

    def feed_forward(self, inputs: list):
        output = inputs.copy()
        
        for layer in self.layers:
            output = layer.feed_forward(output)
            print("Output: " + str(output))
        return output

        #add activation functions
import NeuralNetwork as nn
import pygame
from PyGameOperations import resize_results
from PointGenerator import get_point_by_range
from ActivationFunctions import Activation
import sys


pygame.init()



layer_2_linear = nn.NeuralNetwork([2, 2, 1], "LINEAR")
layer_1_linear = nn.NeuralNetwork([2, 1], "LINEAR")

layer_2_sig = nn.NeuralNetwork([2, 2, 1], "SIGM")
layer_1_sig = nn.NeuralNetwork([2, 1], "SIGM")

layer_2_binary = nn.NeuralNetwork([2, 2, 1], "BINARY_STEP")
layer_1_binary = nn.NeuralNetwork([2, 1], "BINARY_STEP")

screen = pygame.display.set_mode((640,480))

points = []
points_number = 10000
for i in range(points_number):
        x, y = get_point_by_range((-2, 2))
        points.append([x, y])


layer_2_results = []
#feed layer 2 linear NN
for point in points:
        result = layer_2_linear.feed_forward([point])
        layer_2_results.append((point, result))

#draw layer 2 linear
width = 640
height = 640
resized_layer_2_results = resize_results(layer_2_results, (width, height))

screen = pygame.display.set_mode((width, height))
for (point, result) in resized_layer_2_results:
        if result[0][0] > 2.0:
                color = (255, 0, 0)
        else:
                color = (0, 0, 255)
        pygame.draw.circle(screen, color, point, 4, 0)

pygame.display.update()

quit = False
while not quit:
        for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                        pygame.quit()
                        sys.exit()
                        quit = True

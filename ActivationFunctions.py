import math
from enum import Enum

class Activation(Enum):
    SIGMOID = "SIGM"
    LINEAR = "LINEAR"
    BINARY = "BINARY_STEP"

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def linear(x):
    return x

def binary_step(x):
    if x < 0:
        return 0

    return 1
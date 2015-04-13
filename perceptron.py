import random


class Perceptron:
    def __init__(self):
        self.weights = [
            random.uniform(-1, 1),
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        ]

    def get_weights(self):
        return self.weights

    def activate(self, number):
        if number > 0:
            return 1
        else:
            return -1

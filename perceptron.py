import random


class Perceptron:
    learning_rate = 0.01

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

    def feedforward(self, inputs):
        total = 0
        for each in xrange(0, len(inputs)):
            total += inputs[each] * self.weights[each]

        return self.activate(total)

    def train(self, inputs, desired):
        guess = self.feedforward(inputs)
        error = desired - guess
        for each in xrange(0, len(inputs)):
            self.weights[each] += self.learning_rate * error * inputs[each]

        return self.weights

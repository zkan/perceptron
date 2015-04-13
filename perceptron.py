class Perceptron:
    weights = [0, 0, 0]

    def get_weights(self):
        return self.weights

    def activate(self, number):
        if number > 0:
            return 1
        else:
            return -1

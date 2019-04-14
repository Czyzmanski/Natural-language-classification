from random import random
from sys import path
path.append('../util')
import vectors as ve


class Perceptron:

    def __init__(self, act_fun, learning_rate, dim, positive_class):
        self.act_fun = act_fun
        self.learning_rate = learning_rate
        self.dim = dim + 1
        self.positive_class = positive_class
        self.W = [random() for i in range(dim)]

    def learn(self, accuracy, training, epsilon=0.01, max_epochs=1000):
        correct, acc, epochs = 0, 0, 0
        traceback = []

        while acc < accuracy and epochs <= max_epochs:
            correct = 0
            for observation in training:
                exp_output = 1 if observation[-1] == self.positive_class else 0
                X = observation[:-1]
                X.append(-1)
                output = self.classify(X)
                if abs(output - exp_output) <= epsilon:
                    correct += 1
                self.delta_rule(X, exp_output, output)
                # print(observation, output)
                # ve.normalize(self.W)
            acc = correct / len(training)
            traceback.append(acc)
            epochs += 1

        return traceback

    def classify(self, X):
        net = ve.dot_product(self.W, X)
        return self.act_fun(net)

    def delta_rule(self, X, expected_output, real_output):
        coef = (expected_output - real_output) * self.learning_rate
        T = ve.multiply_vect_by_num(X, coef)
        self.W = ve.vectors_sum(self.W, T)

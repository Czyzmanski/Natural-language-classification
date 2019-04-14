from perceptron import Perceptron


class Layer:

    def __init__(self, num_of_neurons, act_fun, learning_rate, neuron_dim, classes):
        self.classes = classes
        self.neurons = [Perceptron(act_fun, learning_rate, neuron_dim, classes[i]) for i in range(num_of_neurons)]

    def train(self, training_data, accuracy=0.98):
        for ordinal, neuron in enumerate(self.neurons):
            traceback = neuron.learn(accuracy, training_data)
            print(self.classes[ordinal], traceback)

    def classify(self, observation):
        outputs = [neuron.classify(observation) for neuron in self.neurons]
        mx_ord, mx_output = 0, outputs[0]
        for i in range(1, len(outputs)):
            if outputs[i] > mx_output:
                mx_output = outputs[i]
                mx_ord = i
        return self.classes[mx_ord]

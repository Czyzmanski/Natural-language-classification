import os
from random import shuffle
import dataprep as dp
from layer import Layer
from sys import path
path.append('../util')
import actfun as af

train_path = input('Please input path to directory with training data:\n').strip()
test_path = input('Please input path to directory with testing data:\n').strip()
learning_rate = float(input('Please input learning rate:\n').strip())

train_dir = sorted(os.listdir(train_path))
test_dir = sorted(os.listdir(test_path))

training_data = dp.prepare_data(train_path, train_dir)
test_data = dp.prepare_data(test_path, test_dir)

shuffle(training_data)
shuffle(test_data)

num_of_cl = len(train_dir)
num_of_attr = len(training_data[0]) - 1

layer = Layer(num_of_cl, af.uni_sigmoid, learning_rate, num_of_attr, train_dir)
layer.train(training_data)

correct = 0
for observation in reversed(test_data):
    prediction = layer.classify(observation[:-1])
    if prediction == observation[-1]:
        correct += 1
    print(observation, prediction)
print('Accuracy: {:.2f}'.format(correct / len(test_data)))

while True:
    text = dp.filter_input(input('Please input your text:\n').strip())
    X = dp.get_observation_input(text)
    print('Prediction: {}'.format(layer.classify(X)))

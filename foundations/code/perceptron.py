from code.utils import load_data, sign
import numpy as np


class Perceptron:
    def __init__(self, iterations, shuffle=False, learning_rate=1.0):
        self.iterations = iterations
        self.shuffle = shuffle
        self.learning_rate = learning_rate
        self.update = 0

    def fit(self, x, y):
        n_samples, n_features = x.shape
        self.w = np.zeros(n_features)
        index = list(range(n_samples))
        if self.shuffle:
            np.random.shuffle(index)

        for iter in range(self.iterations):
            flag = False
            for num in index:
                y_ = sign(np.dot(self.w, x[num]))
                if y_ != y[num]:
                    flag = True
                    self.w = self.w + self.learning_rate * y[num] * x[num]
                    self.update += 1
            if not flag:
                break

    def predict(self, x):
        return sign(np.dot(self.w, x))


if __name__ == '__main__':
    path = './data/hw1_15_train.dat'
    x, y = load_data(path)
    # -----question 15------
    model = Perceptron(10000)
    model.fit(x, y)
    print('answer 15 = {}'.format(model.update))
    # -----question 16------
    np.random.seed(6)
    updates = []
    for i in range(2000):
        model = Perceptron(10000, shuffle=True)
        model.fit(x, y)
        updates.append(model.update)
    result = np.mean(updates)
    # print(updates)
    print('answer 16 = {}'.format(result))
    # -----question 17------
    np.random.seed(8)
    updates = []
    for i in range(2000):
        model = Perceptron(10000, shuffle=True, learning_rate=0.5)
        model.fit(x, y)
        updates.append(model.update)
    # print(updates)
    result = np.mean(updates)
    print('answer 17 = {}'.format(result))

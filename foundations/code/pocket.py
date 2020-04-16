from code.utils import load_data, sign
import numpy as np


class Pocket:
    def __init__(self, shuffle=False, learning_rate=1.0, updates=100):
        self.shuffle = shuffle
        self.learning_rate = learning_rate
        self.updates = updates

    def fit(self, x, y):
        n_samples, n_features = x.shape
        self.w = np.zeros(n_features)
        self.w_pocket = np.zeros(n_features)
        self.w_update = np.zeros(n_features)
        index = list(range(n_samples))
        if self.shuffle:
            np.random.shuffle(index)
        x = x[index]
        y = y[index]
        acc = 0
        while True:
            count = 0
            for num in range(n_samples):
                if sign(np.dot(self.w, x[num])) * y[num] <= 0:
                    self.w = self.w + self.learning_rate * y[num] * x[num]
                    self.updates -= 1
                    pred = self.predict(x)
                    acc_ = self.acuracy(pred, y)
                    if acc_ > acc:
                        acc = acc_
                        self.w_pocket = self.w
                    if self.updates == 0:
                        return

    def predict(self, x):
        return sign(np.dot(x, self.w))

    def error(self, pred, y):
        return np.sum(pred != y) / len(y)

    def acuracy(self, pred, y):
        return np.sum(pred == y) / len(y)


if __name__ == '__main__':
    train_path = './data/hw1_18_train.dat'
    test_path = './data/hw1_18_test.dat'
    x_train, y_train = load_data(train_path)
    x_test, y_test = load_data(test_path)
    np.random.seed(9)
    error = []
    for i in range(2000):
        x_ = x_train.copy()
        y_ = y_train.copy()
        model = Pocket(shuffle=True, updates=50)
        model.fit(x_, y_)
        model.w = model.w_pocket
        pred = model.predict(x_test)

        acc = model.acuracy(pred, y_test)
        error.append(1 - acc)
    # print(error)
    print('answer 18 = {}'.format(np.mean(error)))

    np.random.seed(8)
    error = []
    for i in range(2000):
        model = Pocket(shuffle=True, updates=50)
        x_ = x_train.copy()
        y_ = y_train.copy()
        model.fit(x_, y_)
        pred = model.predict(x_test)
        acc = model.acuracy(pred, y_test)
        error.append(1 - acc)
    # print(error)
    print('answer 19 = {}'.format(np.mean(error)))

    np.random.seed(8)
    error = []
    for i in range(2000):
        model = Pocket(shuffle=True, updates=100)
        model.fit(x_train, y_train)
        model.w = model.w_pocket
        pred = model.predict(x_test)
        acc = model.acuracy(pred, y_test)
        error.append(1 - acc)
    # print(error)
    print('answer 20 = {}'.format(np.mean(error)))

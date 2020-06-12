import numpy as np
from utils import sigmoid


def load(path):
    f = open(path)
    x = []
    y = []
    for line in f.readlines():
        data = line.strip().split(' ')
        feature = data[0: -1]
        feature.append('1')
        x.append(feature)
        y.append(data[-1])

    x = np.array(x, dtype=np.float)
    y = np.array(y, dtype=np.int).reshape((-1, 1))
    return x, y


class LogisticRegression(object):
    def __init__(self, iterations, learning_rate, SGD=False):
        self.iterations = iterations
        self.learning_rate = learning_rate
        self.SGD = SGD

    def fit(self, x, y):
        n_samples, n_features = x.shape
        self.w = np.zeros((n_features, 1))
        for i in range(self.iterations):
            # y_pred = sigmoid(np.dot(x, self.w))
            # grads = np.dot(y_pred - y, x)
            if self.SGD:
                index = i % n_samples
                x_ = x[index, :]
                y_ = y[index, :]
                grads = sigmoid(- y_ * np.dot(x_, self.w)) *\
                    (- y_ * x_)
            else:
                grads = sigmoid(- y * np.dot(x, self.w)) * \
                    (- y * x)

                grads = np.sum(grads, axis=0) / n_samples
            self.w = self.w - self.learning_rate *\
                grads.reshape((n_features, 1))
            # print(self.w)
            loss = self.accuracy(x, y)
            # if i % 100 == 0:
            #    print("{} ites train loss: {}".format(i, loss))

    def predict(self, x):
        mask = np.dot(x, self.w) < 0  # 这里之前一直错误写成0.5
        y_pred = np.ones((x.shape[0], 1))
        y_pred[mask] = -1
        return y_pred

    def accuracy(self, x, y):
        n_samples = x.shape[0]
        y_pred = self.predict(x)
        acc = np.sum(y == y_pred) / n_samples
        return acc


if __name__ == "__main__":
    train_path = './data/hw3_train.dat'
    test_path = './data/hw3_test.dat'
    x_train, y_train = load(train_path)
    # y_train[y_train < 0] = 0
    x_test, y_test = load(test_path)
    # y_test[y_test < 0] = 0
    model = LogisticRegression(iterations=2000, learning_rate=0.001)
    model.fit(x_train, y_train)
    acc = model.accuracy(x_test, y_test)
    print("answer 18 = {}".format(1-acc))
    model = LogisticRegression(iterations=2000, learning_rate=0.01)
    model.fit(x_train, y_train)
    acc = model.accuracy(x_test, y_test)
    print("answer 19 = {}".format(1-acc))
    model = LogisticRegression(iterations=2000, learning_rate=0.001, SGD=True)
    model.fit(x_train, y_train)
    acc = model.accuracy(x_test, y_test)
    print("answer 20 = {}".format(1-acc))

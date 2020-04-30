import numpy as np
from utils import sign


def load(path):
    f = open(path)
    x = []
    y = []
    for line in f.readlines():
        data = line.strip().split(' ')
        feature = data[0: -1]
        x.append(feature)
        y.append(data[-1])

    x = np.array(x, dtype=np.float)
    y = np.array(y, dtype=np.int)
    return x, y


class Stump:
    def __init__(self):
        self.s = None
        self.theta = None

    def _fit(self, x, y):
        x_ = np.sort(x)
        theta = [(x_[i] + x_[i + 1]) / 2 for i in range(len(x_) - 1)]
        err1 = []
        err2 = []
        for i in range(len(theta)):
            y_ = sign(x - theta[i])
            # s = 1
            err_1 = np.sum(y_ != y) / len(x)
            err1.append(err_1)
            # s = -1
            err_2 = np.sum(-y_ != y) / len(x)
            err2.append(err_2)
        min1, min2 = np.min(err1), np.min(err2)
        if min1 < min2:
            s = 1
            theta = theta[np.argmin(err1)]
            e_in = min1
        else:
            s = -1
            theta = theta[np.argmin(err2)]
            e_in = min2
        e_out = 0.5 + 0.3 * s * (np.abs(theta) - 1)
        return e_in, e_out, s, theta

    def fit(self, x, y):
        if x.ndim == 1:
            E_in, E_out, self.s, self.theta = self._fit(x, y)
        else:
            e_in = []
            e_out = []
            si = []
            thetas = []
            for n_feature in range(x.shape[1]):
                x_temp = x[:, n_feature]
                err_in, err_out, s, theta = self._fit(x_temp, y)
                e_in.append(err_in), e_out.append(err_out), si.append(s), thetas.append(theta)
            min_index = np.argmin(e_in)
            E_in = e_in[min_index]
            E_out = e_out[min_index]
            self.dimension = min_index
            self.s = si[min_index]
            self.theta = thetas[min_index]

        return E_in, E_out

    def predict(self, x):
        if x.ndim != 1:
            x = x[:, self.dimension]
        y = self.s * sign(x - self.theta)
        return y


if __name__ == '__main__':
    # generate data
    # question 17 18
    E_in = []
    E_out = []
    for i in range(5000):
        data_size = 20
        x = np.random.uniform(-1, 1, data_size)
        noise_rate = 0.2
        noise = sign(np.random.uniform(0, 1, data_size) - noise_rate)
        y = sign(x) * noise

        stump = Stump()
        e_in, e_out = stump.fit(x, y)
        E_in.append(e_in)
        E_out.append(e_out)
    print("answer 17 = {}".format(np.mean(E_in)))
    print("answer 18 = {}".format(np.mean(E_out)))

    train_path = './data/hw2_train.dat'
    test_path = './data/hw2_test.dat'
    x_train, y_train = load(train_path)
    x_test, y_test = load(test_path)
    stump = Stump()
    e_in, e_out = stump.fit(x_train, y_train)
    print("answer 19 = {}".format(np.mean(e_in)))
    y_pred = stump.predict(x_test)
    e_out = np.sum(y_pred != y_test) / len(y_test)
    print("answer 20 = {}".format(np.mean(e_out)))


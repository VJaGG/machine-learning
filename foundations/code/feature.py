import numpy as np


def sign(x):
    return 1 if x > 0 else -1


def func(x1, x2):
    return sign(x1**2 + x2**2 - 0.6)


def generate(nums):
    data = []
    for i in range(nums):
        x1 = np.random.uniform(-1, 1)
        x2 = np.random.uniform(-1, 1)
        y = func(x1, x2)
        if np.random.rand(1) < 0.1:
            y = -y
        data.append([1, x1, x2, y])
    data = np.array(data)
    return data


def transform(nums):
    data = []
    for i in range(nums):
        x1 = np.random.uniform(-1, 1)
        x2 = np.random.uniform(-1, 1)
        y = func(x1, x2)
        if np.random.rand(1) < 0.1:
            y = -y
        data.append([1, x1, x2, x1*x2, x1*x1, x2*x2, y])
    data = np.array(data)
    return data


def regression_closed_form(x, y):
    w_lin = np.dot(np.dot(np.linalg.pinv(np.dot(x.T, x)), x.T), y)
    return w_lin


if __name__ == "__main__":

    # error_rate = []
    # for i in range(1000):
    #     data = generate(1000)
    #     x = data[:, 0:3]
    #     y = data[:, -1]
    #     w_lin = regression_closed_form(x, y)
    #     pred = np.dot(x, w_lin)
    #     correct = pred * y < 0
    #     res = np.sum(correct)
    #     rate = res * 1.0 / x.shape[0]
    #     error_rate.append(rate)
    # print('answer 13 = {}'.format(np.mean(error_rate)))

    error_rate = []
    min_error = float("inf")
    for i in range(1000):
        data = transform(1000)
        x = data[:, 0:-1]
        y = data[:, -1]
        w_lin = regression_closed_form(x, y)
        pred = np.dot(x, w_lin)
        error = pred * y < 0
        res = np.sum(error)
        rate = res * 1.0 / x.shape[0]
        if rate < min_error:
            w_best = w_lin
        error_rate.append(rate)
    print('answer 14 = {}'.format(w_best))
    # print('transform error rate {}'.format(np.mean(error_rate)))
    error_rate = []
    for i in range(1000):
        data = transform(1000)
        x = data[:, 0:-1]
        y = data[:, -1]
        pred = np.dot(x, w_lin)
        error = pred * y < 0
        res = np.sum(error)
        rate = res * 1.0 / x.shape[0]
        error_rate.append(rate)
    print('answer 15 = {}'.format(np.mean(error_rate)))

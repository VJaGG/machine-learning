import numpy as np


def load_data(path):
    f = open(path)
    x = []
    y = []
    for line in f.readlines():
        data = line.strip().split('\t')
        feature = data[0].split(' ')
        feature.insert(0, '1')
        x.append(feature)
        y.append(data[-1])
    x = np.array(x, dtype=np.float)
    y = np.array(y, dtype=np.int)
    return x, y


def sign(x):
    if type(x) is np.ndarray:
        n_samples = x.shape[0]
        result = np.ones(n_samples)
        result[x <= 0] = -1
        return result
    else:
        if x <= 0:
            return -1
        else:
            return 1

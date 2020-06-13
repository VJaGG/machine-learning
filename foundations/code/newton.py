import numpy as np


def func(u, v):
    res = np.exp(u) + np.exp(2 * v) + np.exp(u * v) +\
     u * u - 2 * v * u + 2 * v * v - 3 * u - 2 * v
    return res


def gradient(u, v):
    du = np.exp(u) + v * np.exp(u * v) + 2 * u \
        - 2 * v - 3
    dv = 2 * np.exp(2 * v) + u * np.exp(u * v) \
        - 2 * u + 4 * v - 2
    return np.array([[du], [dv]])


def hessian(u, v):
    f_uu = np.exp(u) + v * v * np.exp(u * v) + 2
    f_uv = np.exp(u * v) + u * v * np.exp(u * v) - 2
    f_vv = 4 * np.exp(2 * v) + u * u * np.exp(u * v) + 4
    f_vu = np.exp(u * v) + np.exp(u * v) * u * v - 2
    return np.array([[f_uu, f_uv], [f_vu, f_vv]])

# grad = gradient(0, 0)
# print(grad)
# hess = hessian(0, 0)
# print(hess)
# hess_1 = np.linalg.pinv(hess)
# print(hess)
# print(hess @ hess_1)
# print("grad = ", grad)
# print("hess_1 = ", hess_1)
# print(hess_1 @ grad)
# print("------")


u = 0
v = 0
print("newton method:")
for i in range(5):
    grad = gradient(u, v)
    hess = hessian(u, v)
    hess_1 = np.linalg.pinv(hess)
    update = np.array([[u], [v]]) - hess_1 @ grad
    u = update[0][0]
    v = update[1][0]
print(u, v)
print(func(u, v))

u = 0
v = 0
print("gradient method")
for i in range(5):
    grad = gradient(u, v)
    u = u - 0.01 * grad[0][0]
    v = v - 0.01 * grad[1][0]
print(u, v)
print(func(u, v))

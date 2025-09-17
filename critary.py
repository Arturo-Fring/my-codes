# find critary
import numpy as np

x_test = np.array([(-5, 2), (-4, 6), (3, 2), (3, -3), (5, 5), (5, 2), (-1, 3)])
y_test = np.array([1, 1, 1, -1, -1, -1, -1])
w = np.array([-8/3, -2/3, 1])

# здесь продолжайте программу
x = np.array(x_test)
one = np.ones((x_test.shape[0], 1))
X = np.hstack([one, x])

margin = X@w*y_test
condition = margin < 0
Q = np.sum(condition)
print(Q)

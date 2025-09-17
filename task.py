import numpy as np
import matplotlib.pyplot as plt

# Всё для прямой:
A = [2, 0]
B = [7, 7]

w = np.array([-2.8, 1.4, -1])


def y_line(x): return -(w[0] + w[1]*x)/w[2]


print(w[0]+w[1]*9+w[2]*6)

x_line = np.linspace(-10, 10, 10)
y_line = y_line(x_line)

x_test = [(9, 6), (2, 4), (-3, -1), (3, -2), (-3, 6), (7, -3), (6, 2)]

# здесь продолжайте программу
# Выделили данные, пригодится для построения
x = np.array(x_test)  # 7 и 2
x1 = x[:, 0]
x2 = x[:, 1]

# решающая функция имеет вид:
# f(x)=w0+w1x1+w2x2

one = np.ones((x.shape[0], 1))
X = np.hstack([one, x])

h = X@w
predict = np.sign(h)
print(h)

# Отображение результатов
colors = ['red' if p == -1 else 'blue' for p in predict]
plt.scatter(x1, x2, c=colors, s=50, label='Points')

plt.plot(x_line, y_line, marker='*', markersize='4')
plt.show()

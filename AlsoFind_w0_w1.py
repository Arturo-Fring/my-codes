import numpy as np

# псевдослучайные числа образуют одну и ту же последовательность (при каждом запуске)
np.random.seed(0)
x = np.arange(-1.0, 1.0, 0.1)  # аргумент [-1; 1] с шагом 0,1


def model_a(xx, ww): return (
    ww[0] + ww[1] * xx + ww[2] * xx ** 2 + ww[3] * xx ** 3)  # модель


Y = np.sin(x * 5) + 2 * x + np.random.normal(0,
                                             0.1, len(x))  # вектор целевых значений


# обучающая выборка для поиска коэффициентов w модели a
X = np.array([[1, xx, xx**2, xx**3] for xx in x])

# здесь продолжайте программу
w = np.linalg.inv((X.T@X))@X.T@Y

print(w)

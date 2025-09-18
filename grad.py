import numpy as np

# исходная функция, которую нужно аппроксимировать моделью a(x)


def func(x: np.ndarray) -> np.ndarray:
    return 0.1 * x**2 - np.sin(x) + 5.0

# модель: a(x) = w0 + w1*x + w2*x^2 + w3*x^3  ==  w^T s(x)
# модель базируется на весах и входных признаках


def model_a_row(w: np.ndarray, s_row: np.ndarray) -> float:
    return float(s_row @ w)


# --- данные -------------------------------------------------------------
# точки по оси X на [-5; 5] с шагом 0.1 (включая 5.0)

#
coord_x = np.arange(-5.0, 5.0, 0.1)        # shape (n,)
# целевые значения, shape (n,)
coord_y = func(coord_x)
n = coord_x.shape[0]

# матрица признаков S: столбцы [1, x, x^2, x^3], shape (n, 4)
S = np.column_stack([np.ones_like(coord_x),
                     coord_x,
                     coord_x**2,
                     coord_x**3]).astype(float)

# --- параметры градиентного спуска -------------------------------------
# можно вектором (разные lr для каждого параметра) или скаляром
eta = np.array([0.1, 0.01, 0.001, 0.0001], dtype=float)   # shape (4,)
w = np.zeros(4, dtype=float)                               # начальные веса
N = 200                                                    # число итераций

print(S.shape)
print(w.shape)

# --- градиентный спуск --------------------------------------------------
# Q(w) = (1/n) * sum_i (a(x_i) - f(x_i))^2  = (1/n) * ||S w - y||^2
for _ in range(N):
    preds = S @ w                      # a(x_i)
    errors = preds - coord_y           # a(x_i) - f(x_i)
    grad = (2.0 / n) * (S.T @ errors)  # dQ/dw = 2/n * S^T (S w - y)
    w -= eta * grad                    # шаг обновления

# --- итоговые значения --------------------------------------------------
Q_value = (1.0 / n) * np.sum((S @ w - coord_y)**2)

# переменные, которые обычно ждут автотесты
w = tuple(w)            # веса модели (w0, w1, w2, w3)
Q = float(Q_value)      # значение среднего квадратичного риска


# при необходимости можно посмотреть:
print("w =", w)
print("Q =", Q)

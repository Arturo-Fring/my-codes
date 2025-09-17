# margin
import numpy as np
import matplotlib.pyplot as plt

# Образы:
x_test = np.array([[1, -5, 2], [1, -4, 6], [1, 3, 2],
                  [1, 3, -3], [1, 5, 6], [1, 9, 2]])

# Веса:
A = np.array([5, 4])
B = np.array([-4, 0])

p = (B-A)
# Ax+By+C=0
A_coef = p[1]   # A = p_y = -4
B_coef = -p[0]  # B = -p_x = 9

C = -(A_coef*A[0]+B_coef*A[1])

w = [C, A_coef, B_coef]

# Целевые значение
y_test = np.array([1, 1, 1, -1, -1, -1])

# Проверка "вектора" весов:
# if y_test[0] == 1 and w@x_test[0]

# Margin определяется как "решающая функция", умноженная на целевое значение
margin = np.multiply(x_test@w, y_test)

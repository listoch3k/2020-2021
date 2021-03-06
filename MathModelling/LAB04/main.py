import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Без затуханий и воздействий внешней силы
w = math.sqrt(12)
g = 0.00

# Правая часть уравнения
def f(t):
    f = 0
    return f


# Вектор функция для решения системы дифференциальных уравнений
def y(x, t):
    dx1 = x[1]
    dx2 = - w * w * x[0] - 2 * g * x[1] - f(t)
    return dx1, dx2


# Вектор начальных условий
x0 = np.array([1, 2])

# Интервал
t = np.arange(0, 60, 0.05)

# Решаем дифф. уравнения
x = odeint(y, x0, t)

# Переписываем отдельно
y1 = x[:, 0]
y2 = x[:, 1]

# Графики
plt.plot(y1, y2)
plt.grid(axis='both')
plt.show()


# С затуханием и без воздействия внешней силы
w2 = math.sqrt(10)
g2 = 5


# Правая часть уравнения
def f2(t_2):
    f2 = 0
    return f2


# Вектор функция для решения системы дифференциальных уравнений
def y22(x_2, t_2):
    dxx1 = x_2[1]
    dxx2 = - w2 * w2 * x_2[0] - 2 * g2 * x_2[1] - f2(t_2)
    return dxx1, dxx2


# Вектор начальных условий
x_2_0 = np.array([1, 2])

# Интервал
t_2 = np.arange(0, 60, 0.05)

# Решаем дифф. уравнения
x_2 = odeint(y22, x_2_0, t_2)

# Переписываем отдельно
yy1 = x_2[:, 0]
yy2 = x_2[:, 1]

# Графики
plt.plot(yy1, yy2)
plt.grid(axis='both')
plt.show()


# С затуханием и под воздействием внешней силы
w3 = math.sqrt(7)
g3 = 3.5


# Правая часть уравнения
def f3(t_3):
    f3 = 7 * np.sin(3*t_3)
    return f3


# Вектор функция для решения системы дифференциальных уравнений
def y33(x_3, t_3):
    dxxx1 = x_3[1]
    dxxx2 = - w3 * w3 * x_3[0] - 2 * g3 * x_3[1] - f3(t_3)
    return dxxx1, dxxx2


# Вектор начальных условий
x_3_0 = np.array([1, 2])

# Интервал
t_3 = np.arange(0, 60, 0.05)

# Решаем дифф. уравнения
x_3 = odeint(y33, x_3_0, t_3)

# Переписываем отдельно
yyy1 = x_3[:, 0]
yyy2 = x_3[:, 1]

# Графики
plt.plot(yyy1, yyy2)
plt.grid(axis='both')
plt.show()

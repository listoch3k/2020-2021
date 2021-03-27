import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x0 = 11  # Количество людей, знающий о товаре в начальный момент времени
N = 1005  # Аудитория
t = np.arange(0, 12, 0.01)  # Длительность компании


# Функция отвечающая за платную рекламу
def k1(t):
    g = 0.84
    return g


def k2(t):
    g = 0.000022
    return g


def k3(t):
    g = 0.74 * np.sin(t)
    return g


# Для задания
def k4(t):
    g = 0.007
    return g


def p1(t):
    v = 0.00022
    return v


def p2(t):
    v = 0.74
    return v


def p3(t):
    v = 0.35 * np.cos(t)
    return v


# Для задания
def p4(t):
    v = 0.0007
    return v


# Уравнение, описывающее распространение рекламы
def f1(x, t):
    xd1 = (k1(t) + p1(t) * x) * (N - x)
    return xd1


def f2(x, t):
    xd2 = (k2(t) + p2(t) * x) * (N - x)
    return xd2

def f3(x, t):
    xd3 = (k3(t) + p3(t) * x) * (N - x)
    return xd3


# Платная реклама - ноль
def f4(x, t):
    xd4 = (p4(t) * x) * (N - x)
    return xd4


# Сарафанное радио - ноль
def f5(x, t):
    xd5 = k1(t) * (N - x)
    return xd5


# Решение ОДУ
x1 = odeint(f1, x0, t)
x2 = odeint(f2, x0, t)
x3 = odeint(f3, x0, t)
x4 = odeint(f4, x0, t)
x5 = odeint(f5, x0, t)

# График для случая 1
plt.plot(t, x1)
plt.show()

# График для случая 2
plt.plot(t, x2)
plt.show()

# Момент времени с максимальной скоростью
t[np.argmax(x2[1:].reshape(1, 1199)/t[1:] + 1)]

# График для случая 3
plt.plot(t, x3)
plt.show()

plt.plot(t, x1, label='Случай №1')
plt.plot(t, x2, label='Случай №2')
plt.plot(t, x3, label='Случай №3')
plt.legend()
plt.show()

plt.plot(t, x4, label='Сарафанное радио')
plt.plot(t, x5, label='Платная реклама')
plt.legend()
plt.show()
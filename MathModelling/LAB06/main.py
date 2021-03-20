import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

a = 0.2  # Коэффицент заболеваемости
b = 0.1  # Коэффицент выздоровления
n = 17000  # Общая численность популяции
i0 = 116  # Колличество инфицированных особей
r0 = 16  # Количество здоровых особей с иммунитетом

s0 = n - i0 - r0  # Количество особей восприимчивых к болезни


# Случай № 1, когда I(0) <= I*
def syst(x, t):
    dx0 = 0
    dx1 = - b * x[1]
    dx2 = b * x[1]
    return dx0, dx1, dx2


x0 = [s0, i0, r0]  # Начальные значения
t = np.arange(0, 200, 0.01)
y = odeint(syst, x0, t)

plt.plot(t, y[:, 0], label='S(t)')
plt.plot(t, y[:, 1], label='I(t)')
plt.plot(t, y[:, 2], label='R(t)')
plt.title('I(0) <= I*', fontsize=15, fontweight=1000)
plt.legend()
plt.show()


# Случай № 2, когда I(0) > I*
def syst2(x, t):
    ddx0 = -a * x[0]
    ddx1 = a * x[0] - b * x[1]
    ddx2 = b * x[1]
    return ddx0, ddx1, ddx2

yy = odeint(syst2, x0, t)

plt.plot(t, yy[:, 0], label='S(t)')
plt.plot(t, yy[:, 1], label='I(t)')
plt.plot(t, yy[:, 2], label='R(t)')
plt.title('I(0) > I*', fontsize=15, fontweight=1000)
plt.legend()
plt.show()

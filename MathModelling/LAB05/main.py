import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


a = 0.23  # Коэффицент естественной смертности хищников
b = 0.43  # Коэффицент естественного прироста жертв
c = 0.053  # Коэффицент увеличения числа хищников
d = 0.033  # Коэффицент смертности жертв


def system2(x, t):
    dx0 = -a * x[0] + c * x[0] * x[1]
    dx1 = b * x[1] - d * x[0] * x[1]
    return dx0, dx1


x0 = [8, 14]  # Начальные значения x и y (Популяция хищников и популяция жертв

t = np.arange(0, 100, 0.1)

y = odeint(system2, x0, t)

y2 = y[:, 1]  # Массив хищников
y1 = y[:, 0]  # Массив жертв

plt.plot(t, y1, label='Хищники')
plt.plot(t, y2, label='Жертвы')
plt.legend()
plt.show()

# Построение графика зависимости изменения численности хищников от изменения численности жертв
plt.plot(y1, y2)
plt.plot(8, 14, 'ro', label='Начальное состояние')
plt.plot(b/d, a/c, 'go', label='Стационарное состояние')
plt.legend()
plt.grid(axis='both')
plt.show()
---
# Front matter
lang: ru-RU
title: "Лабораторная работа #4"
subtitle: "Модель гармонических колебаний. Вариант 11"
author: "Баулин Егор Александрович, учебная группа: НКНбд-01-18"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Построить фазовый портрет гармонического осциллятора и решить уравнения гармонического осциллятора для следующих случаев
	- Колебания гармонического осциллятора без затуханий и без действий внешней силы $\ddot {x} + 12x = 0$
	- Колебания гармонического осциллятора c затуханием и без действий внешней силы $\ddot {x} + 10 \dot {x} + 5x = 0$
	- Колебания гармонического осциллятора c затуханием и под действием внешней силы $\ddot {x} + 7 \dot {x} + 7x = 0.7sin(3t)$

На интервале $t \in [0; 60]$(шаг 0.05) с начальными условиями $x_0 = 1, y_0 = 2$


# Выполнение лабораторной работы

## Теоретическое введение

   Уравнение свободных колебаний гармонического осциллятора имеет следующий вид:

$$ \ddot {x} + 2 \gamma \dot {x} + w_0^2x = f(t) $$

$x$ — переменная, описывающая состояние системы (смещение грузика, заряд
конденсатора и т.д.)

$t$ — время

$w$ — частота

$\gamma$ — затухание

   Обозначения:

$$ \ddot{x} = \frac{\partial^2 x}{\partial t^2}, \dot{x} = \frac{\partial x}{\partial t}$$


   При отсутствии потерь в системе получаем уравнение консервативного осциллятора, энергия колебания которого сохраняется во времени:

$$ \ddot {x} + w_0^2x = 0 $$


   Для однозначной разрешимости уравнения второго порядка необходимо задать два начальных условия вида:

$$ \begin{cases} x(t_0) = x_0 \\ \dot{x}(t_0) = y_0 \end{cases} $$

   Уравнение второго порядка можно представить в виде системы двух уравнений первого порядка:

$$ \begin{cases} \dot{x} = y \\ \dot{y} = -w_0^2x \end{cases} $$

   Начальные условия для системы примут вид:

$$ \begin{cases} x(t_0) = x_0 \\ y(t_0) = y_0 \end{cases} $$

   Независимые переменные x, y определяют пространство, в котором «движется» решение. Это фазовое пространство системы, поскольку оно двумерно будем называть его фазовой плоскостью.
   
   Значение фазовых координат x, y в любой момент времени полностью определяет состояние системы. Решению уравнения движения как функции времени отвечает гладкая кривая в фазовой плоскости. Она называется фазовой траекторией. Если множество различных решений (соответствующих различным начальным условиям) изобразить на одной фазовой плоскости, возникает общая картина поведения системы. Такую картину, образованную набором фазовых траекторий, называют фазовым портретом.

Код на Python:

```
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
```

Без затухания и воздействия внешней силы (рис. 1)

![Колебания без затухания и воздействия внешней силы](image/plot1.png){ #fig:001 width=70% }

С затуханием без воздействия внешней силы (рис. 2)

![Колебания с затуханием без воздействия внешней силы](image/plot2.png){ #fig:002 width=70% }

С затуханием и под воздействием внешней силы (рис. 3)

![Колебания с затуханием и под воздействием внешней силы](image/plot3.png){ #fig:003 width=70% }

## Ответы на вопросы

### Запишите простейшую модель гармонических колебаний
Простейшим видом колебательного процесса являются простые гармонические колебания, которые описываются уравнением $x = x_m cos (wt + f0)$. 
    

### Дайте определение осциллятора
Осциллятор — система, совершающая колебания, то есть показатели которой периодически повторяются во времени.


### Запишите модель математического маятника

Уравнение динамики принимает вид: $$\frac{d^2 \alpha}{d t^2} + \frac{g}{L} sin{\alpha} = 0$$ В случае малых колебаний полагают $sin{\alpha} = \alpha$. В результате возникает линейное дифференциальное уравнение $$\frac{d^2 \alpha}{d t^2} + \frac{g}{L} \alpha = 0$$ или $$\frac{d^2 \alpha}{d t^2} + \omega^2 \alpha = 0$$

### Запишите алгоритм перехода от дифференциального уравнения второго порядка к двум дифференциальным уравнениям первого порядка
Пусть у нас есть дифференциальное уравнение 2-го порядка:
$$ \ddot {x} + w_0^2x = f(t) $$

Для перехода к системе уравнений первого порядка сделаем замену (это метод Ранге-Кутты):
$$ y = \dot{x} $$

Тогда получим систему уравнений:
    $$ \begin{cases} y = \dot{x} \\ \dot{y} = - w_0^2x \end{cases}$$
    
### Что такое фазовый портрет и фазовая траектория?
Фазовый портрет — это то, как величины, описывающие состояние системы, зависят друг от друга.
Фазовая траектория — кривая в фазовом пространстве, составленная из точек, представляющих состояние динамической системы в последовательные моменты времени в течение всего времени эволюции.

# Выводы

 - Построил фазовый портрет гармонического осциллятора и решил уравнения гармонического осциллятора:
	- Колебания гармонического осциллятора без затуханий и без действий внешней силы.
	- Колебания гармонического осциллятора c затуханием и без действий внешней силы.
	- Колебания гармонического осциллятора c затуханием и под действием внешней силы.



---
## Front matter
lang: ru-RU
title: Лабораторная работа 2. Исследование протокола TCP и алгоритма управления очередью RED.
author:	Баулин Егор Александрович

## Formatting
toc: false
slide_level: 2
theme: metropolis
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
---


# Цель работы

Ознакомиться с протоколом TCP и алгоритмом управления очередями RED.

# Задачи

 - Реализовать 	пример алгоритма RED на NS-2 с получением графиков через xgraph.
 - Внести изменения в скрипт заменив TCP Reno на NewReno и Vegas, а также сравнить результаты.

# Моделируемая в примере сеть

![Схема моделируемой сети](image/1.png){ #fig:2 width=70% }

# Графики для первого случая

![График динамики размера окна TCP (Reno)](image/2.jpg){ #fig:2 width=70% }

# Графики для первого случая

![График динамики длины очереди и средней длины очереди(Reno)](image/3.jpg){ #fig:3 width=70% }

# При смене Reno на NewReno

![График динамики размера окна TCP (NewReno)](image/4.jpg){ #fig:4 width=70% }

# При смене Reno на NewReno

![График динамики длины очереди и средней длины очереди(NewReno)](image/5.jpg){ #fig:5 width=70% }

# При смене Reno на Vegas

![График динамики размера окна TCP (Vegas)](image/6.jpg){ #fig:6 width=70% }

# При смене Reno на Vegas

![График динамики длины очереди и средней длины очереди(Vegas)](image/7.jpg){ #fig:7 width=70% }

# Сравнение результатов

Результаты изменений Reno на NewReno практически не дали разницы в показателях. В свою очередь протокол Vegas сокращает частоту колебания размера окна, но амплитуда колебаний выше, чем при NewReno

# Выводы

 - Ознакомился с алгоритмом управления очередями RED, произвел моделирование на NS-2, а также сравнил результаты с разными TCP.
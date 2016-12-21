import numpy as np
import init
import matplotlib.pyplot as plt
from solution import *

print('Коэффициенты целевой функции:')
c = init.c
c = np.matrix([[1], [3]])
print(c)
print('Коэффициенты ограничений:')
a = init.a
a = np.matrix([[3, 2], [1, 2], [-1, 1], [0, 1], [-1, 0], [0, -1]])
print(a)
print('Правая часть ограничений:')
b = init.b
b = np.matrix([[12], [6], [1], [2], [0], [0]])
print(b)

vect = sysSolution(a, b)
x = vect[:][0]
y = vect[:][1]

plt.plot(x, y, 'ro')
plt.show()

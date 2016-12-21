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

for z in range (x.size):
    for w in range (init.n):
        print(w, '/n')
        if(a[w, 0] * x[z] + a[w, 1] * y[z] > b[w]):
            x[z] = 0
            y[z] = 0

plt.plot(x, y, 'green')
plt.show()

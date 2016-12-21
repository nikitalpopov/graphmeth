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
        if(a[w, 0] * x[z] + a[w, 1] * y[z] > b[w]):
            x[z] = 0
            y[z] = 0

pointsX = np.empty(x.size)
pointsY = np.empty(x.size)
count = 0
for i in range (x.size):
    if(x[i] != 0 or y[i] != 0):
        pointsX[count] = x[i]
        pointsY[count] = y[i]
        count += 1

plt.plot(pointsX, pointsY, 'green')
plt.show()

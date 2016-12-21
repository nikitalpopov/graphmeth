import numpy as np
import init
import matplotlib.pyplot as plt
from solution import *
from jarvis import *

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

counts = 0 # Количество наших точек
for i in range (x.size):
    if(x[i] != 0 or y[i] != 0):
        counts += 1

if(counts < x.size):
    counts += 1
pointsX = np.zeros(counts)
pointsY = np.zeros(counts)
if(counts < x.size):
    pointsX[counts - 1] = 0
    pointsY[counts - 1] = 0
count = 0 # Счётчик только для цикла
for i in range (x.size):
    if(x[i] != 0 or y[i] != 0):
        pointsX[count] = x[i]
        pointsY[count] = y[i]
        count += 1

A = np.vstack((pointsX, pointsY)).T
P = list(range(counts))
H = [A[0]]
del P[0]

print(jarvis(A, counts))

#plt.plot(pointsX, pointsY, 'green')
#plt.show()

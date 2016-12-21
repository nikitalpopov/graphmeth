import numpy as np
import init
import matplotlib.pyplot as plt
from solution import *
from jarvis import *

# Ввод начальных условий:

print('Коэффициенты целевой функции:')
c = init.c
c = np.matrix([[1], [3]])
print(c.T)
print('Коэффициенты ограничений:')
a = init.a
a = np.matrix([[3, 2], [1, 2], [-1, 1], [0, 1], [-1, 0], [0, -1]])
print(a)
print('Правая часть ограничений:')
b = init.b
b = np.matrix([[12], [6], [1], [2], [0], [0]])
print(b)

# Находим точки пересечения ограничений

vect = sysSolution(a, b)
x = vect[:][0]
y = vect[:][1]

# Убираем лишние точки (не удовлетворяющие ограничениям)

for z in range(x.size):
    for w in range(init.n):
        if a[w, 0] * x[z] + a[w, 1] * y[z] > b[w]:
            x[z] = 0
            y[z] = 0

# Убираем лишние точки (0,0), полученные на предыдущем шаге

counts = 0  # Количество наших точек
for i in range(x.size):
    if not x[i] == 0 or not y[i] == 0:
        counts += 1

if counts < x.size:
    counts += 1
pointsX = np.zeros(counts)
pointsY = np.zeros(counts)
if counts < x.size:
    pointsX[counts - 1] = 0
    pointsY[counts - 1] = 0

count = 0  # Счётчик только для цикла
for i in range(x.size):
    if not x[i] == 0 or not y[i] == 0:
        pointsX[count] = x[i]
        pointsY[count] = y[i]
        count += 1

# Строим мво по полученному множеству точек

A = np.vstack((pointsX, pointsY)).T
P = list(range(counts))
H = jarvis(A, counts)
del P[0]

# Находим максимальное значение целевой функции

newPointsX = np.zeros(counts + 1)
newPointsY = np.zeros(counts + 1)
maxZ = c[0] * newPointsX[0] + c[1] * newPointsY[0]
indexMax = 0
for i in range(counts):
    newPointsX[i] = pointsX[H[i]]
    newPointsY[i] = pointsY[H[i]]
    if c[0] * newPointsX[i] + c[1] * newPointsY[i] > maxZ:
        maxZ = c[0] * newPointsX[i] + c[1] * newPointsY[i]
        indexMax = i
newPointsX[counts] = newPointsX[0]
newPointsY[counts] = newPointsY[0]

# Выводим результат вычисления в консоль

print('')
print(float(c[0]), ' * ', float(newPointsX[indexMax]), ' + ', float(c[1]), ' * ', float(newPointsY[indexMax]), ' = ', float(maxZ))

# Строим график со многоугольником, отображающим допустимое
# множество решений, и отмеченной точкой, в которой
# целевая функция достигает максимальное значение

plt.plot(newPointsX, newPointsY, 'green')
plt.scatter(newPointsX[indexMax], newPointsY[indexMax])
plt.show()

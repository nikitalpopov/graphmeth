import numpy as np
from numpy import linalg as la
import init


def sysSolution(a, b):

    # Решение всех возможных пар линейных уравнений из 'A * x = b'
    # для получения координат точек пересечения ограничений.
    # На вход подаются:
    # a - матрица (init.n, init.k)
    # b - вектор (init.n, 1)
    # На выходе получаем:
    # vect - матрица координат точек пересечения (1ая строка - x1, 2ая – x2)

    counter = 0
    vect = np.zeros((init.k, init.n*init.n))
    isUsable = True

    for i in range(init.n):
        for k in range(i + 1, init.n, 1):
            tempA = np.zeros((2, 2))
            tempB = np.zeros((2, 1))
            tempX = np.zeros((2, 1))
            if not i == k:
                for l in range(init.k):
                    tempA[0][:] = a[i][:]
                    tempA[1][:] = a[k][:]
                    tempB[0][0] = b[i][0]
                    tempB[1][0] = b[k][0]

                if not la.det(tempA) == 0:
                    tempX = la.solve(tempA, tempB)

                for z in range(tempX.size):
                    if tempX[z][0] < 0:
                        isUsable = False

                if isUsable:
                    for m in range(init.k):
                        vect[m][counter] = tempX[m][0]
            counter += 1

    return vect

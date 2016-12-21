import numpy as np
from numpy import linalg as la
import init
import newton


def sysSolution(a, b):  # решение 'A * x = b'
    counter = 0
    vect = np.zeros((init.k, init.n*init.n))
    tempA = np.zeros((2, 2))
    tempB = np.zeros((2, 1))
    tempX = np.zeros((2, 1))
    isUsable = True

    for i in range(init.n):
        for k in range(i + 1, init.n, 1):
            tempA = np.zeros((2, 2))
            tempB = np.zeros((2, 1))
            tempX = np.zeros((2, 1))
            if not i == k:
                print(i, ' != ', k)
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
    # print('Vect:', vect)
    return vect


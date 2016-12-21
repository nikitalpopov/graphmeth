import numpy as np
from numpy import linalg as la
import init
import newton


def sysSolution(a, b): # решение 'A * x = b'
    counter = 0
    vect = []
    tempA = np.zeros((2, 2))
    tempB = np.zeros((2, 1))
    tempX = np.zeros((2, 1))
    print('tempX: ',tempX)
    for i in range(init.n):
        for k in range(init.n):
            tempA = np.zeros((2, 2))
            tempB = np.zeros((2, 1))
            tempX = np.zeros((2, 1))
            if not i == k:
                # print(i, ' != ', k)
                for l in range(init.k):
                    # print(l)
                    tempA[0][:] = a[i][:]
                    tempA[1][:] = a[k][:]
                    tempB[i][0] = b[i][0]
                    tempB[k][0] = b[k][0]
                # print(tempA)
                # print(tempX)
                # print(tempB)

                while la.norm(tempB) >= 0.000001:
                    c = la.solve(tempA, tempB)
                    tempX -= c

                for m in range(init.k):
                    vect[counter][m] = tempX[0][m]
            print(counter)
            counter += 1
    print('Vect:', vect)


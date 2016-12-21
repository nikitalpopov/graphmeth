import numpy as np
from numpy import linalg as la


def newton(x, J, sys):
    # c - приращение к x
    c = la.matrix_power(J, -1)
    c = np.matmul(c, sys)
    for i in range(10):
        c[i]
    return c


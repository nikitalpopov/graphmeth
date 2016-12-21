import numpy as np
import init
import scipy.optimize
from solution import *

print('Коэффициенты целевой функции:')
c = init.c
c = np.matrix([[1], [2]])
print(c)
print('Коэффициенты ограничений:')
a = init.a
a = np.matrix([[5, 3], [3, 4], [1, 0]])
print(a)
print('Правая часть ограничений:')
b = init.b
b = np.matrix([[1], [2], [3]])
print(b)

x = sysSolution(a, b)

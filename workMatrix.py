import numpy as np
import numpy.linalg as la
import matplotlib.pylab as plt

# first = []
# second = []
# F = input(np.matrix(" First{} and Second{} ").format(first,second))
# print(F)

A = np.matrix([[1,3], [2,5]])
B = np.matrix([[4,7], [9,2]])
C = A + 5
D = A + B
E = A * B
X = np.matrix([[2],[3]])
Y = A * X

print(A)
print(B)
print(C)
print(D)
print(E)
print(Y)

#Matrix Diision

B_det = la.det(B)
print(B_det)
B_inv = la.inv(B)
print(B_inv)

print(B_det * B_inv)



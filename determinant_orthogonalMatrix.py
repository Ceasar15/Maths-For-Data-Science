import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import pandas as ps


# Determinant
A = np.array([[0,-1],[1,0]])
print("\n Determinant of 2x2: ",round(la.det(A)))

B = np.array([[2,4,3],[3,5,2],[5,4,2]])
print("\n Determinant of 3x3 matrix: ",round(la.det(B)))

print("\n Matrix: ")
print(A)
print("\n Inverse of A: ")
print(la.inv(A))
print("\n Transpose: ")
print(A.T)


#Eigen Values and Eigen Vectors
C= np.array([[2,4],[6,7]])
eigenvals = la.eigvals(C)
eigval, eigvec = la.eig(C)

print("\n Original matrix: ")
print(C)
print("\n Just the Eigen values: ")
print(eigenvals)
print("\n Eigen Values: ")
print(eigval)
print("\n Eigen vectors: ")
print(eigvec)

D=np.array([[1,2,3,4],[2,2,2,2],[4,3,2,5],[3,2,4,3]])
eigenValss = la.eigvals(D)
print("\n Original 4x4 Matrix: ")
print(D)
print("\n Eigen values of a 4x4 matrix: ")
print(eigenValss)



F = np.array([[1,4],[4,1]])
eigval, eigvec = la.eig(A)

v1=eigvec[:,0]
v2=eigvec[:,1]

Av1 = F @ v1
Av2 = F @ v2

v1_mag = np.sqrt(np.sum(np.square(eigvec[:,0])))
v2_mag = np.sqrt(np.sum(np.square(eigvec[:,1])))

print("Original Matrix: ")
print(F)
print("\n The Eigen Decomposition")
print("The Eigen values: ")
print(eigval)
print("The Eigen vectors: ")
print(eigvec)
print("\n The Magnitude of v1 and v2: ")
print(round(v1_mag), round(v2_mag))


plt.plot([0, v1[0]], [0, v1[1]], 'black', label='v1', linewidth=2)
plt.plot([0, v2[0]], [0, v2[1]], 'yellow',label='v2', linewidth=2)
plt.plot([0, Av1[0]], [0, Av1[1]], 'r:')
plt.plot([0, Av2[0]], [0, Av2[1]], 'b:')

plt.legend()
plt.grid()
plt.axis('square')
plt.axis([-2,4,-3,4])
plt.show()






import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt


C= np.array([30,10])
D = np.array([10, 35])
F = D + 9

TFM_Rotate2 = np.array([[0,-1],[-1,0]])
G= TFM_Rotate2 @ C

TFM_Rotate3 = np.array([[-1,1],[-1,1]])
H= TFM_Rotate3 @ C

plt.plot([0, D[0]], [0, D[1]], 'pink' , label='vector1', linewidth=2 )
plt.plot([0, C[0]], [0, C[1]], 'blue' , label='vector2', linewidth=2 )
plt.plot([0, F[0]], [0, F[1]], 'yellow' , label='Scale', linewidth=2 )
plt.plot([0, G[0]], [0, G[1]], 'brown' , label='90 Rotation', linewidth=2) 
plt.plot([0, H[0]], [0, H[1]], 'gold' , label='270 Rotation', linewidth=2) 
plt.plot([40,     0], [0,  0], 'black')
plt.plot([0,    0], [0,   50], 'black')
plt.plot([-40,     0], [0,  0], 'black')
plt.plot([0,    0], [0,   -50], 'black')

plt.title(" An Example of a Graph using matplotlib")
plt.legend()
plt.axis((-70,70,-70,70))
plt.axis("on")
plt.grid()
plt.show()

A = np.array([[2,3],[4,5]])
B = np.array([[5],[3]])
v1 = A @ B
print(v1)


TFM_Rotate = np.array([[0,1],[-1,0]])
v2 = TFM_Rotate @ C
print(v2)

plt.plot([0, C[0]],  [0, C[1]],  'y',  label = 'Main', linewidth =2)
plt.plot([0, v1[0]], [0, v1[1]], 'r', label= 'Vector Mul', linewidth=2 )
plt.plot([0, v2[0]], [0, v2[1]], 'g', label='Rotation', linewidth=2)


plt.legend()
plt.axis("square")
plt.axis((-30,35,-30,50))
plt.grid()
plt.show()




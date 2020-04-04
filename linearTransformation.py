import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt


v1 = np.array([1,1])
plt.plot([0, v1[0]], [0, v1[1]], 'b' , label='v', linewidth=2 )
plt.plot([1,0],[0,0], 'g', label='ihat')
plt.plot([0,0],[0,1], 'r', label='jhat')


plt.legend()
plt.axis('square')
plt.axis((-0.5,1.5,-0.5,1.5))
plt.grid()
plt.show()

TFM_Scale = np.array([[2,0], [0,3]])
v2 = TFM_Scale @ v1
print("Scale along diagonal transform matrix ")
print(TFM_Scale)
print(v2)

TFM_Rotate = np.array([[0,-1],[-1,0]])
v3=TFM_Rotate @ v1
print("90 degrees clockwise rotation: ")
print(TFM_Rotate)
print(v3)

TFM_Shear = np.array([[1,1],[0,1]])
v4 = TFM_Shear @ v1
print("Shear along x-axis: ")
print(TFM_Shear)
print(v4)

#Plot Transformation
plt.plot([0, v1[0]], [0, v1[1]], label='v', linewidth=2)
plt.plot([0, v2[0]], [0, v2[1]], label='Scale', linewidth=2)
plt.plot([0, v3[0]], [0, v3[1]], label="Rotate", linewidth=2)
plt.plot([0, v4[0]], [0, v4[1]], label='Shear',  linewidth= 2)


plt.legend()
plt.axis('square')
plt.axis((-3,4,-2,5))
plt.grid()
plt.show()



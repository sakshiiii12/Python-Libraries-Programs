#Multiplication of 2D Matrix.

import numpy as np

mat1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
mat2 = np.array([[7,8,9], [1,0,1], [1,2,3]])
mat3 = np.zeros_like(mat1)
for i in range(0,3):
    for j in range(0, 3):
        val = 0
        for k in range(0, 3):
            val = val + mat1[i][k] * mat2[k][j]
            mat3[i][j] = val
print(mat3)

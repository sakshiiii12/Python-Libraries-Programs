#Transpose Of A Matrix.

import numpy as np

mat = np.array([[1,2,3], [4,5,6], [7,8,9]])
for i in range(0, mat.shape[0]):
    for j in range(0, mat.shape[1]):
        print(mat[j][i], end=" ")
    print()

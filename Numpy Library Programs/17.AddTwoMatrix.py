#Addition of 2D Matrix.

import numpy as np

mat1 = np.array([[1,2,3], [4,5,6,], [7,8,9]])
mat2 = np.array([[6,4,5], [2,4,0], [7,3,1]])
if(mat1.shape[0] == mat2.shape[0] and mat1.shape[1] == mat2.shape[1]):
    for i in range(0, mat1.shape[0]):
        for j in range(0, mat2.shape[1]):
            print(mat1[i][j] + mat2[i][j], end= " ")
        print()
else:
    print("Addition Not Posssible")

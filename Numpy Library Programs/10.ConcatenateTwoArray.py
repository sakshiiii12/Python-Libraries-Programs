#How do you concatenate two Numpy arrays along the first axis.

import numpy as np

ar1 = np.array([1,2,3,4,5])
ar2 = np.array([6,7,8,9,10])
result = np.concatenate((ar1, ar2), axis = 0)
print(result)

#Get the common items between two arrays.

import numpy as np

ar1 = np.array([1,2,3,4,5])
ar2 = np.array([4,5,6,7,8])
common = np.intersect1d(ar1, ar2)
print("Common Items Between Two Arrays are:",common)

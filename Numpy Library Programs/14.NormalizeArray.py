#Normalize a 1D NumPy array.

import numpy as np

ar = np.array([1,2,3,4,5])
norm = (ar - ar.mean()) / (ar.std())
print(norm)

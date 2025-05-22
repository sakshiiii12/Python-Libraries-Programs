#Normalize a 1D array (Min-Max Normalization).

import numpy as np

ar = np.array([1,2,3,4,5])
norm_ar = (ar-ar.min()) / (ar.max()-ar.min())
print("Normalize Array:",norm_ar)

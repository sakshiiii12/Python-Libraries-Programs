#Get the positions of NaNs in a NumPy array.

import numpy as np

ar = np.array([1, 2, np.nan, 4, np.nan])
nan_indices = np.where(np.isnan(ar))
print(nan_indices)

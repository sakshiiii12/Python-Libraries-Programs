#Sort an array in ascending and descending order.

import numpy as np

ar = np.array([21,78,90,56,89,100,45,32,12,0])
li1 = list(ar)
min_sort = []
for i in ar:
    min_sort.append(min(li1))
    li1.remove(min(li1))
print("Ascending Order:",min_sort)

print("\n")

ar = np.array([21,78,90,56,89,100,45,32,12,0])
li2 = list(ar)
max_sort = []
for i in ar:
    max_sort.append(max(li2))
    li2.remove(max(li2))
print("Descending Order:",max_sort)

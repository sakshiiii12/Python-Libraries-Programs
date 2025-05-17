#Write a program to replace all even numbers in a Numpy array with -1.

import numpy as np

#This is first method to solve this program.
ar = np.array([1,2,3,4,5,6,7,8,9,10])
ar [ar%2 == 0] = -1
print(ar)

print("--------------------------------")

#This is the second method to solve this program.
for i in ar:
    if(i%2==0):
        i=-1
        print(i)
print(ar)

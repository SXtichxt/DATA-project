import numpy as np

#Atribute numpy 

#1. ndim 
a = np.array([1,2,3,4,5])
print(a.ndim)

#2. d.type

a = np.array([1,2,3])
print(a.dtype)

#3. shape
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a.shape)

#4. size
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a.size)

#5.itemsize
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a.itemsize)
import numpy as np

#flatten
a = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(a.flatten())
print(a)

#ravel
b = a.ravel()
b[0] = 9
print(b)
print(a)
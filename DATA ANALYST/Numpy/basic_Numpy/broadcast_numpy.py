import numpy as np

#Broadcast is dim of arr not equal
a = np.array([[1,2],[3,4],[5,6]])
a[:,0] = (a[:,0]+10)
print(a)
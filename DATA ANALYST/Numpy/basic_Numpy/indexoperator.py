import numpy as np

a  = np.array([1,2,3,4,5,6,7,8,9])

index = np.array([0,1,2])
index1 = np.array([1,2])
print(a[index])

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b[np.ix_([0,1,2],[0,1])])


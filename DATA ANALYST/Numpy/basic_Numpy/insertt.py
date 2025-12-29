import numpy as np

# #insert 1 dim
# a = np.array([1,2,4,5,8,11])
# b = np.insert(a,[0,3,5,4],[99,88,77,66])
# print(b)

#insert 2 dim
c = np.array([[1,2,3,4],[5,6,7,8]])
d = np.insert(c,1,[100], axis = 1)
e = np.insert(c,1,[10,20,30,40],axis = 0)
f = np.insert(c,4,[[11],[22]],axis = 1)
print(d)
print(e)
print(f)
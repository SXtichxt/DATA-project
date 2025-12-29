import numpy as np 
a = np.arange(1,11)
print(a)
b = np.delete(a,0)
print(b)

#delete 2 dim
c = np.arange(1,13).reshape(4,3)
print(c)
d = np.delete(c,2,axis = 0)
print(d)
e = np.delete(c,2,axis = 1)
print(e)
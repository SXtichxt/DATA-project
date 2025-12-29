import numpy as np

#1dim
a = np.array([10,5,4,6,99,100,50,30])
print(a.sum)
print(a.prod())
print(a.min())
print(a.max())
print(a.argmax())#position max in arr
print(a.argmin())#position min in arr

#axis 2 dim ---> axis0 = column , axis1 =row
b = np.array([[10,20,30],[40,50,90],[80,100,5]])
c = np.min(b,axis = 1)
d = np.max(b,axis = 0)
print(c)
print(d)
import numpy as np

a = np.arange(1,13,1)
b = a.reshape(3,4)
print(b)

a.resize(4,3)
print(a)
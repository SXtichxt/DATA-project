import numpy as np

#split
a  = np.arange(1,21)
print(a)
b = np.split(a,4) #split 4 part, each part has 5 value
print(b)
a = a.reshape(5,4)
print(np.hsplit(a,4))
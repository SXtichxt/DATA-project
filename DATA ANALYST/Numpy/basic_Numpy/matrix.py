import numpy as np

#Zero matrix

# a = np.zeros(5)
# print(a)

# a = np.zeros(5,dtype = int)
# print(a)

# b = np.zeros([3,4],dtype = int)
# print(b)

# b = np.zeros((3,3),dtype = int)
# print(b)

#ONE matrix

# a = np.ones(5)
# print(a)

# a = np.ones([3,4,3])
# print(a)

#Full matrix

# a = np.full(5,9) 
# print(a)

# b = np.full([2,3,4],7.5)
# print(b)

#Empty array

# a = np.empty([3,4])
# print(a)

#Identity matrix
# a = np.identity(3)
# print(a)

# b = np.identity(4,dtype = int)
# print(b)

# c = np.eye(5)
# print(c)

d = np.eye(3,4)
print(d)

e = np.eye(5,k = 1)
print(e)

e = np.eye(5,k = -1)
print(e)
import numpy as np

# #สร้างarray n มิติ
# arr = np.array(1) # 0 มิติ
# print(arr)
# print(arr.ndim) # 0 มิติ

# a = np.array([1,2,3]) # 1 มิติ
# print(a.ndim) # 1 มิติ

# li = [1,2,3,4]
# b = np.array(li) #list to arr
# print(b)

# tu = (1,2,3,4,5) 
# c = np.array(tu) # tuple to arr
# print(c)

# d = np.array((1,2,3,3,7))
# print(d)

# aa = np.array([[1,2,3],[4,5,6]]) # 2 dim
# print(aa[0,2],aa[1,2])
# print(aa.ndim) # 2 dim

# li = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# bb = np.array(li) # 2 dim
# print(bb)

# tu = ((1,2,3),(4,5,6),(7,8,9))
# cc = np.array(tu)
# print(cc)

aaa = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]]) #3 dim
print(aaa)
print(aaa.ndim)
print(aaa.shape) # depth, row , column (3,2,3) 
print(aaa[0,1,2] + aaa[-1,-1,-3])

# aaa = np.zeros((2,3,4))
# print(aaa)
# print(aaa.ndim)
# print(aaa.shape)
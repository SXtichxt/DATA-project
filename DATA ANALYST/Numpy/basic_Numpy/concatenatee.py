import numpy as np 

# #concatenate = connect arr
# a = np.array([[3,4,2,6],[11,22,33,44]])
# print(a)

# b = np.array([[8,6,5,10],[99,88,77,66]])
# c = np.concatenate((a,b))
# print(c)

# #append = add value in arr at last index
# d = np.append(a,100) # 1 dim
# print(d)

# #append 2 dim
# e = np.append(b,[[111,222,333,444],[555,666,777,888]], axis = 0)
# f = np.append(a,[[-1],[-2],[-3],[-4]],axis = 1)
# print(e)
# print(f)

#vstack
a = np.array([[1,2,3,4],
              [5,6,7,8]])
new_rows = np.array([[111,222,333,444],
                     [555,666,777,888]])
new_cols = np.array([[4.1, 4.2, 4.3, 4.4, 4.5],
                     [8.1, 8.2, 8.3, 8.4, 8.5],
                     [444.1, 444.2, 444.3, 444.4, 444.5],
                     [888.1, 888.2, 888.3, 888.4, 888.5]])
e = np.vstack((a, new_rows))
f = np.hstack((e, new_cols))
print(f)
import numpy as np

# 1 dim
a = np.array([10, 20, 30, 40, 50])
print(a[::-1])
# print(a[1:4])   # index 1 ถึง 3
# print(a[:3])    # ตั้งแต่ต้นถึง index 2
# print(a[::3])   # ข้ามทีละ 2

# 2 dim
a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(a[0:2, 1:3])   # แถว 0-1, คอลัมน์ 1-2
print(a[1, : ])       # ทุกแถว, คอลัมน์แรก

x = np.array([[1,-2,-3],[4,-5,-9]])
print(x[x>0])
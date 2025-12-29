import numpy as np
# Integer
# Float
# String
# Boolean
# Complex
# Object

#INTEGER
I = np.array([1,2,3,4,5]) 
print(I.dtype) #int 64 bit

I = np.array([1,2,3,4,5], dtype = np.int32) #change to 32 bit
print(I.dtype)

#FLOAT
F = np.array([1.5, 2, 3.5], dtype = float)
print(F.dtype)
print(F)

#STRING
S = np.array(["apple", "banana", "orange"])
print(S)
print(S.dtype) #<u6 Unicode string ความยาวสูงสุด 6 alphabet

#BOOLEAN
B = np.array([True, False, True])
print(B)
print(B.dtype)

#COMPLEX
C = np.array([1+2j,2,3-1j], dtype = complex)
print(C.dtype)
print(C)

#OBJECT
OB = np.array([1, {"apple" : 1}, True, 3.14]) # object
print(OB)
print(OB.dtype)

OB = np.array([1, "apple", True, 3.14]) # U32 tranform all to string
print(OB)
print(OB.dtype)
import numpy as np

# a1 = np.arange(2,dtype=bool)
# a1 = np.arange(12)
# a1 = a1.astype(bool)
# print(a1)

# a2 = np.array([0,22,33],dtype=bool)
# print(a2)


# a3 = np.identity(10,dtype=complex)
# print(a3)

a4 = np.linspace(1,10,7,dtype=np.int16)
print(a4)
print(a4.ndim)
print(a4.itemsize)
print(a4.dtype)
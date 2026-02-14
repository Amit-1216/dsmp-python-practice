import numpy as np
# # import sys

# # a = np.arange(10000000, dtype=np.int8)
# # print(sys.getsizeof(a))
# # print(a.__sizeof__())
# # print(a.nbytes)


# import sys
# import numpy as np
# a = np.arange(100000, dtype=np.int16)
# print(sys.getsizeof(a))
# print(a.__sizeof__())
# print(a)


# # b = [i for i in range (1000)]
# # print(sys.getsizeof(b))
# # print(b)



# L = [11, 11, 22, 33, 22, 22, 22, 44, 55, 66, 44, 11, 22, 66]
# temp = []
# for i in range (len(L)):
#     counter = 0
#     for j in range (len(L)):
#         if L[i] == L[j]:
#             counter += 1
#     temp.append(counter)


# max_val = max(temp)
# print(temp.index(max_val))

# # ----------------------------------------------------------------------------------------------

# L = [11, 11, 22, 33, 22, 22, 22, 44, 55, 66, 44, 11, 22, 66]
# freq = {}

# for i in L:
#     if i not in freq:
#         freq[i] = 1
#     else:
#         freq[i] += 1

# most_occ = max(freq, key=freq.get)
# print(L.index(most_occ))

# # ================================================================================================================================================= # #


# a = np.array([[1,2,np.nan],[4,2,6],[np.nan,np.nan,5]])
# print(a)
# vals = a[~np.isnan(a)]
# """
# > nan will never match an existing dictionary key
# > You will end up storing multiple separate NaN entries in the dictionary
# > Your final max(freq, key=freq.get) will not give the correct most common element
# > The counts will be wrong
# """
# freq = {}
# for i in vals:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# print(freq)
# most_occ = max(freq, key=freq.get)

# a[np.isnan(a)] = most_occ
# print(a)


# # ==================================================================================================================================================== # #

# def check_broadcast (a, b):
#     for i in range (1, min(len(a), len(b))+1):
#         # print(b[i])
#         # print(a[len(a)-i], b[len(b)-i])
#         if a[len(a)-i] != b[len(b)-i]:
#             print(a[len(a)-i], b[len(b)-i])
#             if (a[len(a)-i] == 1) or b[len(b)-i] == 1:
#                 continue
#             return False
        
#         elif a[len(a)-i] == b[len(b)-i]:
#             continue
#         else:
#             return False
        
#     return True

# a = (3, 2, 2)
# b = (1, 1)

# print(check_broadcast(a, b))


# # =============================================================================================================================================== # #

# def BCE (y, y_pred):
#     return -(y * np.log(y_pred) + (1-y) * np.log(1-y_pred))

# actual = np.array([1,0,1,0,1,1,0,1,0,1])
# predicted = np.random.random(10)

# print(BCE(actual,predicted))

# ## ============================================================================================================================================== # #

import numpy as np

# Create a random 3x4 matrix
a = np.random.randint(0, 100, size=(3, 4))
print("Original matrix:\n", a)

# Sort rows based on the maximum value in each row
sorted_matrix = a[np.argsort(np.max(a, axis=1))]

print("\nSorted based on max value in each row:\n", sorted_matrix)










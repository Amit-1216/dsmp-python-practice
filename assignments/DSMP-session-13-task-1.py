# # Q3 -> Write a function to create a 2d array with 1 on the border and 0 inside. Take 2-D array shape as (a,b) as parameter to function.
# import numpy as np
# def numpyArray (a,b):
#     a1 = np.ones(a*b,dtype=int).reshape(a,b)
#     a1[1:a-1,1:b-1] = 0

#     return a1

# prompt1 = int(input("Enter the 1st value: "))
# prompt2 = int(input("Enter the 2nd value: "))
# array1 = numpyArray(prompt1, prompt2)
# print(array1)

# # Q4 -> Create a vector of size 10 with values ranging from 0 to 1, both excluded.
# import numpy as np
# Wrong Approach
# a1 = np.random.random((10))
# for i in range (len(a1)):
#     if a1[i] == 0:
#         a1[i] += 0.1

# Right Approach
# a2 = np.linspace(0,1,12)[1:-1]
# print(a2)

# Q5 --> No

# # Q6 -> Create a 5x5 matrix with row values ranging from 0 to 4.
# import numpy as np
# A = np.zeros(25,dtype=int).reshape(5,5)
# for i in range(len(A)):
#     for j in range(len(A)):
#         # if A[i][j] != 0:
#         A[i][j] = j

# # A = np.tile(np.arange(5), (5,1)) # Alternate Way
# print(A)

# # Q7 -> Consider a random integer (in range 1 to 100) vector with shape (10,2) representing coordinates, and coordinates of a point as array is given.
# # Create an array of distance of each point in the random vectros from the given point. Distance array should be interger type.
# import numpy as np
# a1 = np.random.randint(1,101, (10,2))
# print(a1)

# point = np.array([50, 50])
# distance = []
# for i in range(len(a1)):
#     for j in range(len(a1[0])):
#         if j == 0:
#             p1 = a1[i][j]
#         else:
#             p2 = a1[i][j]
    
#     print(p1)
#     print(p2)
#     res = ((p1 - point[0])**2 + (p2 - point[1])**2)
#     res = np.sqrt(res)
#     distance.append(round(res))
# print(distance)

# # Alternate Way
# import numpy as np
# a1 = np.random.randint(1, 101, (10, 2))
# point = np.array([50, 50])

# distance = np.sqrt(np.sum((a1 - point) ** 2, axis=1))
# distance = np.round(distance).astype(int)
# print(distance)

# # Q8 -> Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
# import numpy as np
# a1 = np.arange(6*7*8).reshape(6,7,8)
# print(a1)
# print(a1[1,5,3])
# print(a1.flat[99])

# # Q9 -> Arrays
# import numpy as np
# s = "11 2 3 4 -8 -10"
# res = ''
# temp = ''
# a1 = []
# for i in range (len(s)):
#     if s[i] != ' ':
#         res += s[i]
#     else:
#         a1.append(float(res))
#         res = ''
# a1.append(float(res))
# a1 = np.array(a1)[::-1]
# # print(res)
# print(a1)
# print(a1.ndim)

# # Q10 -> Elements count
# import numpy as np
# # count = 0
# def count_elements (arr):
#     count = 0 # Good to use it locally, especially with recursion.
#     # global count
#     for i in arr:
#         if isinstance (i, np.ndarray):
#             count += count_elements(i)
#         else:
#             count += 1
#     return count

# arr1 = np.zeros (32).reshape(4,2,2,2)
# print(count_elements(arr1))
# print(arr1)

# # Q11 -> Softmax function
# import numpy as np
# def softmax (arr):
#     result = []
#     if not isinstance (arr, np.ndarray):
#         raise TypeError("Input must be NumPy array.")
#     if arr.ndim != 1:
#         raise ValueError("Input must be 1D array.")
    
#     ezi = np.exp(arr - np.max(arr))
#     sum_exps = np.sum(ezi)

#     for i in ezi:
#         temp = i / sum_exps
#         result.append(temp)
#     return np.array(result)

# a = np.arange(10)
# print(softmax(a))

# # Q12 -> Vertical stack
# import numpy as np
# def v_stack(*args):
#     # Validate all inputs are numpy arrays
#     for arr in args:
#         if not isinstance(arr, np.ndarray):
#             raise TypeError("All inputs must be numpy arrays")
    
#     # Handle empty input case
#     if len(args) == 0:
#         return np.empty((0, 0))
    
#     # Process each array to ensure 2D shape
#     processed = []
#     for arr in args:
#         if arr.ndim == 1:
#             # Convert 1D to 2D row vector
#             processed.append(arr.reshape(1, -1))
#         elif arr.ndim == 2:
#             # Keep 2D arrays as-is
#             processed.append(arr)
#         elif arr.ndim == 3:
#             # Reshape 3D arrays to 2D by combining first two dimensions
#             processed.append(arr.reshape(-1, arr.shape[-1]))
#         else:
#             raise ValueError("Arrays with more than 3 dimensions are not supported")
    
#     # Check all arrays have same number of columns
#     n_cols = processed[0].shape[1]
#     for arr in processed[1:]:
#         if arr.shape[1] != n_cols:
#             raise ValueError("All arrays must have the same number of columns")
    
#     # Vertically stack all processed arrays
#     return np.concatenate(processed, axis=0)

# a = np.array([[[1,2,3],
#                [4,5,6],
#                [7,9,0]]])
# b = np.array([[[11,22,33],
#                [44,55,66],
#                [77,88,99]]])
# x = np.arange(9).reshape(3,3)

# c = v_stack(a,b,x)
# print(c)

# # ------------------ 

# import numpy as np
# def v_stack (*args):
#     # Type validation
#     for array in args:
#         if not isinstance (array, np.ndarray):
#             raise TypeError ("Input must be numpy array")
        
#     # Column validation
#     flag = array.shape[-1]
#     for array in args:
#         if array.shape[-1] != flag:
#             raise ValueError ("All the arrays must contain same number of columns")
        
#     # Main program
#     v_array = []
#     for array in args:
#         if array.ndim == 0:
#             v_array.append(array.reshape(1,1))
#         elif array.ndim == 1:
#             v_array.append(array.reshape(1,-1))
#         elif array.ndim >= 2:
#             v_array.append(array.reshape(-1, array.shape[-1]))

#     return np.concatenate(v_array, axis=0)

# a = np.arange(16).reshape(2,2,2,2)
# b = np.arange(32).reshape(4,2,2,2)
# c = v_stack(a,b)
# print(c)

# # Q13 -> Dates
# import numpy as np
# def date_array (*, start=None, end=None, **kwargs):
#     # validation
#     if kwargs:
#         raise TypeError (f"Unexpected keyword arguments: {', '.join(kwargs.keys())}")
#     try:
#         start_date = start.split('-')
#         end_date = end.split('-')
#         if not (int(start_date[0]) > 0 and int(end_date[0]) > 0 and
#                 1 <= int(start_date[1]) <= 12 and 1 <= int(end_date[1]) <= 12 and
#                 1 <= int(start_date[2]) <= 31 and 1 <= int(end_date[2]) <= 31):
#             raise TypeError("1 Invalid date format: month or day out of range.")
        
#         start_yy, start_mm, start_dd = map(int, start_date)
#         end_yy, end_mm, end_dd = map(int, end_date)

#         if start_yy != end_yy:
#             raise ValueError("Start and End year must me same")

#         if (start_yy, start_mm, start_dd) > (end_yy, end_mm, end_dd):
#             raise ValueError ("Start date must be smaller then End date")

#     except (IndexError):
#         raise TypeError ("2 Invalid date format: it must be like 'yyyy-mm-dd'")
    
#     # # Main logic
#     diff_start_yy, diff_start_mm, diff_start_dd = start_yy - end_yy, start_mm - end_mm, start_dd - end_dd
#     date_arr = []
#     temp = start_dd
#     for i in range (start_mm, end_mm + 1):
#         mm = i
#         # for j in range (start_dd, end_dd + 1):
#         for j in range (abs(start_dd-end_dd) + 1):
#             if temp == end_dd+1:
#                 break
#             if temp > 31:
#                 temp = 1
#             dd = j
#             date_str = f"{start_yy}-{mm}-{temp}"
#             date_arr.append(date_str)
#             temp += 1

#     return np.array(date_arr)
    
# try:
#     a = date_array(start='2020-11-25', end='2020-12-05')
#     print(a)
# except TypeError as e:
#     print("Custom Error:", e)


# # Q14 -> Subtract the mean of each row from a matrix.
# import numpy as np
# a = np.arange(11,110,11,dtype=float).reshape(3,3)
# for row in range (len(a)):
#     mean = a[row].mean()
#     #print(mean)
#     for col in range (len(a[0])):
#         a[row][col] = a[row][col] - mean
# print(a)


# # Q15
# import numpy as np
# a = np.arange(16,dtype=float)
# # print(a,"\n")
# # b = np.arange(25,dtype=float).reshape(5,5)
# # print(b)
## Faster Approach
# if a.ndim == 1 and len(a) >= 2:
#     a[-2], a[-1] = a[-1], a[-2]
# else:
#     for i in range (len(a)):
#         ## if a[i][-2] == a[i][-2]:
#         a[i][-2], a[i][-1] = a[i][-1], a[i][-2]
# print(a)

## Slower Approach
## for i in range (len(a)):
##    for j in range (len(a[0])):
##        if a[i][-2] == a[i][-2]:
##           b[i][-2] = a[i][-1]
##      elif a[i][-1] == a[i][-1]:
##         b[i][-1] = a[i][-2]
##    else:
##       b[i][j] = a[i][j]
## print(b)

# # --------------------------------------------------

# import numpy as np
# def swap_columns(a, col1=-2, col2=-1):
#     if a.ndim == 1 and len(a) >= 2:
#         a[col1], a[col2] = a[col2], a[col1]
#     else:
#         for i in range(len(a)):
#             a[i][col1], a[i][col2] = a[i][col2], a[i][col1]
#     return a

# a = np.arange(16,dtype=float).reshape(4,4)
# print(a)
# print()
# print(swap_columns(a,col1=1,col2=2))


## Q 16 - Replace odd elements in arrays with -1.
# import numpy as np
# def replace (array):
#     if not isinstance (array, np.ndarray):
#         raise ValueError ("Input Must be numpy array")
#     array = array.reshape(-1,len(array[0]))
#     for i in range (len(array)):
#         for j in range (len(array[0])):
#             if array[i][j]%2 != 0:
#                 array[i][j] = -1
#     return array

# a = np.arange(16).reshape(2,2,2,2)
# print(replace(a))

# # -----------------------------------------------
# # Vectroization Approach (Must faster then Recursion | It doesn't changes the dimension of the array)

# import numpy as np
# def replace_odds(array):
#     if not isinstance(array, np.ndarray):
#         raise TypeError("Input must be a NumPy array")
    
#     array[array % 2 != 0] = -1
#     return array
# a = np.arange(16).reshape(2, 2, 2, 2)
# print(replace_odds(a))


# # Q 17 - Given two arrays of same shape make an array of max out of two arrays. (Numpy way)
# import numpy as np
# a=np.array([[[6,3,1,5,8]]])
# b=np.array([[[3,2,1,7,2]]])
## c = np.maximum(a, b) ## Best Approach

## Alternate Way
# a_flat = a.flatten()
# b_flat = b.flatten()
# c_flat = np.empty_like(a_flat)

# for i in range (len(a_flat)):
#     c_flat[i] = max(a_flat[i], b_flat[i])
# c = c_flat.reshape(a.shape)
# print(c)
# print(a.shape)


## Q 18 - 
# import numpy as np
# arr1=np.random.randint(low=1, high=10000, size=40).reshape(8,5)
# print(arr1)
# print(arr1[::,1::2])


## Q 20
import numpy as np
a = np.array([1,2,3])

part1 = np.repeat(a,3)
part2 = np.tile(a,3)
b = np.concatenate([part1,part2])
print(b)


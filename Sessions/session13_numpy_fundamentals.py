# Q1
import numpy as np
import time
# a1 = np.zeros(10)
# print(a1)
# a1[4] = 1
# print(a1)

# ------------------------------------------------------------------------------------------------------------
# Q2
# a = int(input("Enter the 1st number: "))
# b = int(input("Enter the 2nd number: "))

# a2 = np.random.random(a*b).reshape(a,b)
# print(a2)
# print(f"Average of the Array (mean): {a2.mean()}")

# --------------------------------------------------------------------------------------------------------------
# Q3
# import numpy as np
# def func (a, b):
# 	a3 = np.ones(a*b).reshape(a,b)
# 	for i in range(len(a3[0])):
# 		for j in range(len(a3[0])):
# 			if i in range (1,3) and j in range (1,3):
# 			#if a3[i][j] in a3[1:3,1:3]:
# 				a3[i][j] = 0
# 				#print(a1[i])
# 	return a3

# def func (a, b):
# 		a3 = np.ones(a*b).reshape(a,b)
# 		a3 [1:3,1:3] = 0
# 		return a3 
# print(func(4,4))

# --------------------------------------------------------------------------------------------------------------
# # Q4
# a3 = np.linspace(0,1,12)[1:-1]
# print(a3)
# print(a3[1:-1])

# --------------------------------------------------------------------------------------------------------------
# Q5
# a4 = np.eye(3 ,4)
# print(a4)

# --------------------------------------------------------------------------------------------------------------
# Q6
# a5 = np.empty((5,5))
# for i in range (5):
#     for j in range (5):
#         a5[i][j] = j
# print(a5)


# N = 1000  # Change to 1000x1000 matrix
# # Python Loop Approach
# a5 = np.empty((N, N))
# start = time.time()
# for i in range(N):
#     for j in range(N):
#         a5[i][j] = j
# time.sleep(1)
# end = time.time()
# print("Python loop time:", end - start)

# # NumPy Vectorized Approach
# start = time.time()
# a5 = np.tile(np.arange(N), (N, 1))  # Using NumPy's optimized functions
# time.sleep(1)
# end = time.time()
# print("NumPy vectorized time:", end - start)

# --------------------------------------------------------------------------------------------------------------
# Q7
# def calculate_distance (random, point):
#     result = np.empty(10)
#     for i in range (10):
#         distance = np.sqrt((random[i][0] - point[0])**2 + (random[i][1] - point[1])**2)
#         result[i] = distance
#     return result


# a6 = np.linspace(1,99,20).astype(int).reshape(10,2)
# print(a6)
# point = np.array([2,3])

# temp = calculate_distance(a6, point)
# print(temp.astype(int))

# --------------------------------------------------------------------------------------------------------------

a = np.arange(16).reshape(2, 2, 2, 2)
print(a)
print()
a[a % 2 != 0] = -1
print(a)


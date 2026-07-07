import numpy as np

# marks = np.random.randint(1,100,size=(5,4))
# print(marks)
# extra_subject = np.array([41, 87, 72, 36, 92])
# marks = np.concatenate((marks, extra_subject.reshape(5,1)), axis=1)  ## Best practice
# print(marks)

# # ii
# rec1 = np.array([77, 83, 98, 95, 89])
# rec2 = np.array([92, 71, 52, 61, 53])
# marks = np.concatenate((marks, rec1.reshape(1,5), rec2.reshape(1,5)))
# print(marks)
# print("\n")


# # iii

# # temp = np.append(marks, np.sum(marks, axis=1)).reshape(7,6)
# # print(temp)

# total_marks = np.sum(marks, axis=1)
# marks = np.concatenate((marks, total_marks.reshape(-1,1)), axis=1)
# print(marks)



# # iv
# print("\niv")
# temp = marks[np.flip(np.argsort(marks[:,-1]),axis=0)]
# print(temp[:2,])

# #==============================================================================================================


# arr = np.array([[1,2,3,3,1,1],
#                 [0,9,1,2,8,8],
#                 [1,2,3,8,8,8],
#                 [1,2,3,3,1,1]])

# row_wise = np.unique(arr, axis=0)
# print(row_wise)

# print("\n")
# col_wise = np.unique(arr, axis=1)
# print(col_wise)

# #==============================================================================================================

# a = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])
# print("a\n",a)
# a = np.flip(a, axis=0)
# print(a)

# a = np.flip(a, axis=1)
# print(a)


# #==============================================================================================================


# arr = np.array([[1,2,3,4,5],
#                 [10,-3,30,4,5],
#                 [3,2,5,-4,5],
#                 [9,7,3,6,5]])

# x = 6

# temp = np.where(arr > x)
# print(np.unique(temp[0]))


# #==============================================================================================================

# np.random.seed(400)
# arr = np.random.randint(100, 1000, 200).reshape((1, 200))
# print(arr)

# del_item = np.delete(arr, [np.argmin(arr), np.argmax(arr)], axis=1)
# print(del_item)


# #===============================================================================================================




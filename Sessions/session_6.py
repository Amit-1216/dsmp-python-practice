# *args -> allows to pass various number of non-keyworded arguments.

# def multiply (*args):
#     temp = 1
#     for i in args:
#         temp = temp * i
#     print(args)
#     return temp

# print(multiply(1,2,3,4,5,6))

# -------------------------------------------------------------------------------------------------------------------------------------------------------- #

# **kwargs -> Allows us to pass any number of keyword of arguments. Means arguments containing key value pairs like Dictionary

# def display (**kwargs):
#     for key, value in kwargs.items():
#         print(key, '->', value)
#     print(kwargs)

# display(India="Delhi", Japan="Tokyo", USA="Washington DC")

# -------------------------------------------------------------------------------------------------------------------------------------------------------- #

# # Returning Number

# def f ():
#     def x (a, b):
#         return a+b
#     return x
#     # return x()

# print(f()(7,5))
# # print(f())

# -------------------------------------------------------------------------------------------------------------------------------------------------------- #

# def func_a ():
#     print("Inside Function a")

# def func_b (x):
#     print("Inside function b")
#     return x()
#     # return x
# print(func_b(func_a))
# # print(func_b(func_a()))


# -------------------------------------------------------------------------------------------------------------------------------------------------------- #

# string = lambda s : 'a' in s
# # string = lambda s : 'a' if 'a' in s else False
# print(string("Amit"))

# a = lambda num : "Even" if num%2 == 0 else "Odd"
# print(a(76))

# -------------------------------------------------------------------------------------------------------------------------------------------------------- #

# def cube (n):
#     return n**3

# #HOF
# def transform (f,L):
#     output = []
#     for i in L:
#         output.append(f(i))
#     print(output)

# L = [1,2,3,4,5]
# ## transform(cube,L)
# transform(lambda x : x**3,L)

# -------------------------------------------------------------------------------------------------------------------------------------------------------- #

a = tuple(map(lambda x:'even' if x%2 == 0 else 'odd', [1,2,3,4,5,6,7,8,9,10]))
print(a)



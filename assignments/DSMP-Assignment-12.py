# Q1
# def gcd (num1, num2, counter=1):
#     temp = counter + 1
#     if (num2==0):
#         return f"GCD:{num1} CALL:{temp}"
#     return gcd(num2, num1%num2, temp)
# print(gcd(5,10))

# Q2

# class myEnumerate:
#     def __init__ (self,iterable, start=0):
#         self.iterable = iterable
#         self.start = start

#     def __iter__(self):
#         return myEnumerate_iterator(self.iterable, self.start)

# class myEnumerate_iterator:
#     def __init__(self, iterable ,start, counter=0):
#         self.iterable = iterable
#         self.start = start
#         self.counter = counter

#     def __iter__ (self):
#         return self

#     def __next__ (self): 
#         if self.counter >= len(self.iterable):
#             raise StopIteration
        
#         current = self.counter
#         index = self.start
#         self.start += 1
#         self.counter += 1
#         return (index, self.iterable[current])


# # x = myEnumerate([11,22,33])
# # iter_x = iter(x)
# # print(next(iter_x))
# # print(next(iter_x))
# # print(next(iter_x))
# for i,k in myEnumerate([99,24,68], start=10):
#     print(i,k)
# print()
# for i,k in enumerate([99,24,68], start=20):
#     print(i,k)

# x = enumerate({11,22,33})
# iter_x = iter(x)
# print(next(iter_x))

# for i,k in enumerate ("abc"):
#     print(f"{i} : {k}")

# Q3

# class Circle:
#     def __init__ (self, sequence, num):
#         self.sequence = sequence
#         self.num = num

#     def __iter__ (self):
#         return CircleIterator(self.sequence, self.num)

# class CircleIterator:
#     def __init__ (self, sequence, num):
#         self.sequence = sequence
#         self.num = num
#         self.iteration = 0
#         self.counter = 0

#     def __iter__ (self):
#         return self

#     def __next__ (self):
#         if self.iteration >= self.num:
#             raise StopIteration
        
#         current = self.sequence[self.counter]
#         self.counter += 1
#         self.iteration += 1

#         if self.counter >= len(self.sequence):
#             self.counter = 0
        
#         return current
        

# c = Circle("abc", 15)
# print(list(c))

# Q4
# import time

# def calculate_time (func):
#     def wrapper (*args):
#         current = time.time()
#         print(func(*args))
#         return time.time() - current
#     return wrapper

# @calculate_time
# def square():
#     # time.sleep(2)
#     return 99**999

# n = square()
# print(n)

# -----------------------------------

# def sanity_check(data_type):
#     def outer_wrapper(func):
#         def inner_wrapper(*args):
#             # if (type(*args)) == data_type:
#             # if (isinstance(arg, data_type) for arg in args): This does not checks all arguments
#             # if [type(arg) == data_type for arg in args]:
#             # if all(type(arg) == data_type for arg in args):
#             for arg in args:
#                 if (type(arg)!=data_type):
#                     raise TypeError ("Invalid DataType")
#             return func(*args)
#         return inner_wrapper
#     return outer_wrapper

# @sanity_check(int)
# def square(n):
#     return n**2
# x = square(4)
# print(x)

# @sanity_check(int)
# def power (a,b):
#     return a**b
# y = power (2,3)
# print(y)

# @sanity_check(str)
# def display ():
#     return "Hello, Amit"
# z = display()
# print(z)

# Q5
# class Person:
#     def __init__ (self, name, state, city, age):
#         self.name = name
#         self.state = state
#         self.__city = city
#         self.__age = age

#     def address (self):
#         return f"{self.name}, {self.__city}, {self.state}"

# p = Person("Amit", "Maharashtra", "Mumbai", 20)
# print(p.address())

# Q6
# import time
# def timer (iterable):
#     index = 0
#     prev_time = time.time()
#     for i in iterable:
#         current_time = time.time()
#         yield (current_time - prev_time, iterable[index])
#         index += 1
#         prev_time = current_time

# for i in timer('abcd'):
#     print(i)
#     time.sleep(2)
    
# Q7
# def bold(func):
#     def wrappper(*args):
#         return f"<b>{func(*args)}</b>"
#     return wrappper

# def italic(func):
#     def wrappper(*args):
#         return f"<i>{func(*args)}</i>"
#     return wrappper

# def underline(func):
#     def wrappper(*args):
#         return f"<u>{func(*args)}</u>"
#     return wrappper

# @bold
# @italic
# @underline
# def hello():
#     return "Hello World"

# a = hello()
# print(a)

# Q8
# def call_twice(func):
#     def wrapper(*args):
#         func(*args)
#         func(*args)
#     return wrapper

# @call_twice
# def hello(string):
#     print(string)

# hello("Hello, Amit!")


# def my_for_loop (iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(next(iterator))
#         except StopIteration:
#             break

#L = [11,22,33,44,55]
#my_for_loop(L)
# r = range(1,11)
# iter_obj = iter(r)
# print(type(iter_obj))
# my_for_loop(r)

# ------------------------------------------------------------------------------------------------------------------------------------------------ #

# class MyRangeFunction:
#     def __init__ (self,start,stop):
#         self.start = start
#         self.stop = stop

#     def __iter__ (self):
#         return IterOfMyRange(self)

# class IterOfMyRange:
#     def __init__ (self, my_range_obj):
#         self.my_range_obj = my_range_obj

#     def __iter__ (self):
#         return self
    
#     def __next__ (self):
#         if self.my_range_obj.start >= self.my_range_obj.stop:
#             raise StopIteration
        
#         current = self.my_range_obj.start
#         self.my_range_obj.start += 1
#         return current


# r1 = MyRangeFunction(0,11)
# for i in r1:
#     print(i)

# #r1 = MyRangeFunction(0,11)
# #my_for_loop(r1)

# import sys
# print(sys.getsizeof(r1))


# x = MyRangeFunction(0,6)
# print(type(x))

# print(iter(x))


# ---------------------------------------------------------------------------------------------------------------------------------------------------------- #

# def square (num):
#     for i in range (1,num):
#         yield i**2

# x = MyRangeFunction(1,11)

# gen_obj = square(11)
# my_for_loop(gen_obj)

# print(next(gen_obj))

# for i in gen_obj:
#     print(i)


# L = [11,22,33]
# iter_L = iter(L)
# print(iter_L)

# print(iter_L.__next__())
# print(iter_L.__next__())
# print(iter_L.__next__())
# print(iter_L.__next__())


# print(next(iter_L))
# print(next(iter_L))
# print(next(iter_L))
# print(next(iter_L))

# def kanchana_loop (iterable):
#     iter_obj = iter(iterable)
    
#     while True:
#         try:
#             print(next(iter_obj))
#         except StopIteration:
#             break
        

# L = [11,22,33]
# r = range(11,21)
# t = (44,55,66)
# s = {77,88}
# d = {1:2,2:3,3:4}

# kanchana_loop(L)
# kanchana_loop(r)
# kanchana_loop(t)
# kanchana_loop(s)
# kanchana_loop(d)


# class my_range:
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end
        

#     def __iter__ (self):
#         return my_range_iterator(self.start,self.end)

# class my_range_iterator:
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return self
    
#     # def __next__(self):
#     #     try:
#     #         while True:
#     #             if self.start <= self.end:
#     #                 print(self.start)
#     #                 self.start += 1
#     #             else:
#     #                 break
#     #     except StopIteration:
#     #         print("-------------------")

#     def __next__(self):
#         if self.start <= self.end:
#             current = self.start
#             self.start += 1
#             return current
#         else:
#             raise StopIteration

# # for i in my_range(1,10):
# #     print(i)

# # a = my_range(11,21)
# # for i in a:
# #     print(i)

# L = [11,22,33,44,55]
# iter_L = iter(L)
# # print(type(iter_L))
# print(next(iter_L))
# print(next(iter_L))
# print(next(iter_L))
# print(next(iter_L))


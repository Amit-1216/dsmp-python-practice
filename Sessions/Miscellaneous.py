# def function(l: list, s, **args):
#     try:
#         last_element = l[-1]

#         l[int(s)]=10
#         any_element = l[int(s)+10]
#         l[s]=10

#         res = sum(l)
#         print(res)

#         p = args['p']
#         # print(p)
#         return res/last_element * p + any_element
#     except IndexError:
#         print("IndexError: Index Out Of Range")
#     except ValueError:
#         print("ValueError: Invalid value")
#     except TypeError:
#         print("TypeError: operation on different data type")
#     except ZeroDivisionError:
#         print("ZeroDivisionError: Division performed by Zero")
#     except KeyError:
#         print("KeyError: Key not found")
#     except Exception as e:
#         print("Some Error Occured")

# # function([1,2,1], 12)
# # function([1,2,1]*9, '1-2')
# # function([1,'2',1]*9, 12)
# # function([1,'2',1]*9, 12)
# # function([1,2,0]*9, 12)
# # function([1,2,1]*9, 12, p=None)
# function([1,2,0]*9, 12, p=10)

# --------------------------------------------------------------------------------------------------------------------------------------------------------- #

# l = [{0:2},2,3,4,'5', {5:10}]
# s=0
# for i in range(len(l)):
#     try:
#         #You can Edit code from here
#         if type(l[i]) == dict:
#             s += l[i].get(i)
#         else:
#             s += int(l[i])
#     except ValueError:
#         print("ValueError")
#     except IndexError:
#         print("IndexError")
#     except TypeError:
#         print("TypeError")
# print(s)

# --------------------------------------------------------------------------------------------------------------------------------------------------------- #

# try:
#     # Open the file in write mode
#     with open("greeting.txt", "w") as file:
#         # Write data to the file
#         file.write("Hello, Good Morning!!!")
# except IOError as e:
#     # Handle any I/O errors (e.g., file not found, permission denied, etc.)
#     print(f"An I/O error occurred: {e}")
# except Exception as e:
#     # Handle any other unforeseen errors
#     print(f"An unexpected error occurred: {e}")
# else:
#     # This block will execute only if no exceptions are raised
#     print("Data written to the file successfully.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------- #

# class ValueTooLarge (Exception):
#     def __init__ (self, message):
#         super().__init__(message)

# class ValueTooSmall (Exception):
#     def __init__ (self, message):
#         super().__init__(message)

# class GuessError (Exception):
#     def __init__ (self, message):
#         super().__init__(message)

# number = 12
# while True:
#     try:
#         num_inp = int(input("Enter a Number: "))
#         if num_inp < 1:
#             raise GuessError ("Guess Error Enter greater values")
#         elif num_inp > number:
#             raise ValueTooLarge("Value is too large to be guesssed!!!")
#         elif num_inp < number:
#             raise ValueTooSmall("Value is too small to be guessed!!!")
#         else:
#             print("Correct Guess!!!")
#             break
    
#     except ValueError:
#         print("ValueError: Please input integers only")
#     except ValueTooLarge:
#         pass
#     except ValueTooSmall:
#         pass
#     except GuessError as ge:
#         print(ge)
#     except Exception as e:
#         print("Some Error Occured")

# --------------------------------------------------------------------------------------------------------------------------------------------------------- #

# class InvalidAge (Exception):
#     def __init__ (self, message):
#         super().__init__(message)

# class InvalidName (Exception):
#     def __init__ (self, message):
#         super().__init__(message)

# class CastVote:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age
    
#     def can_vote (self):
#         Name = self.name.split()
#         try:
#             if self.name == '' or self.name == ' ' or len(Name) < 2:
#                 raise InvalidName ('InvalidName: Please enter valid name')
#             if self.age < 18 or self.age > 100:
#                 raise InvalidAge ('InvalidAge: Please enter valid age')
#             else:
#                 self.name = ' '.join(Name)
#                 print(f"{self.name.title()} Congratutaions! You can Vote!")
        
#         except InvalidName as e:
#             print(e)
#         except InvalidAge as ia:
#             print(ia)
#         except ValueError as ve:
#             print(ve)

# person1 = CastVote('  AMiit Maurya', 12)
# person1.can_vote()

# --------------------------------------------------------------------------------------------------------------------------------------------------------- #

# class StopIteration (Exception):
#     def __init__ (self, message):
#         super().__init__(message)
#         #Exception.__init__(self, message)

# def infinite_numbers (num):
#     try:
#         if num == 20:
#             raise StopIteration('\nStopIteration: num excedes the maximum iteration')
#         print(num, end=' ')
#         return infinite_numbers(num + 1)
    
#     except StopIteration as si:
#         print(si)

# infinite_numbers(0)


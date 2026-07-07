# n = int(input("Enter a Number: "))
# sum = i = 0
# while i < n+1:
#     i += 1
#     if i%5 == 0:
#         continue
#     sum += i
#     if sum >= 300:
#         temp = sum - i
#         sum = temp
#         break

# print(sum, i)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- #

# res = ''
# for i in range (2000, 3201):
#     if i%7 == 0 and i%5 != 0:
#         res = res + str(i) + ', '    
#     i += 1
# print(res[:-2])

# ----------------------------------------------------------------------------------------------------------------------------------------------------------- #

# def check_even (num):
#     hold = str(num)
#     even_num = 0
#     while num > 0:
#         digit = num % 10
#         if digit % 2 == 0:
#             even_num = (even_num * 10) + digit
#         num //= 10
#     if len(hold) == len(str(even_num)):
#         even_num = str(even_num)
#         return even_num[::-1]
#     else:
#         return ''

# res = []
# for i in range (1000, 3000+1):
#     num = check_even(i)
#     if num != '':
#         res.append(num)
# print(" ".join(res))

#  ----------------------------------------------------------------------------------------------------------------------------------------------------- #

# n = 5 
# for i in range (1, n+1):
#     for j in range (i, 0, -1):
#         print(j, end=' ')
#     print()

# ------------------------------------------------------------------------------------------------------------------------------------------------------- #

# a = [1,2,3,4]
# for i in range (4):
#     for j in range (4):
#         for k in range (4):
#             for l in range (4):
#                 if i != j and j != k and k != l and i != l and i != k and j != l:
#                     print(a[i], a[j], a[k], a[l])

# a = [1,2,3]
# for i in range (3):
#     for j in range (3):
#         for k in range (3):
#             if i != j and j != k and i != k:
#                 print(a[i], a[j], a[k])


# ---------------------------------------------------------------------------------------------------------------------------------------------------------- #

# def float_to_binary(num):
#     if num == 0:
#         return "0.0"
    
#     # Split the number into integer and fractional parts
#     integer_part = int(num)
#     fractional_part = num - integer_part
#     print(integet_part,fractional_part)
    
#     # Convert integer part to binary
#     integer_binary = ""
#     if integer_part == 0:
#         integer_binary = "0"
#     else:
#         while integer_part > 0:
#             integer_binary = str(integer_part % 2) + integer_binary
#             integer_part = integer_part // 2
    
#     # Convert fractional part to binary
#     fractional_binary = ""
#     while fractional_part > 0:
#         # Limit the length of the fractional binary to avoid infinite loops
#         if len(fractional_binary) > 10:
#             break
#         fractional_part *= 2
#         bit = int(fractional_part)
#         if bit == 1:
#             fractional_part -= bit
#             fractional_binary += '1'
#         else:
#             fractional_binary += '0'
    
#     # Combine both parts
#     if fractional_binary:
#         return f"{integer_binary}.{fractional_binary}"
#     else:
#         return integer_binary

# # Take input from the user
# decimal_number = float(input("Enter a float number: "))

# # Convert to binary and print the result
# binary_equivalent = float_to_binary(decimal_number)
# print(f"Binary equivalent: {binary_equivalent}")


#                                   OR                              #


# num = float(input("Enter a Number: "))
# int_part = int(num)
# float_part = num - int_part

# int_binary = ''
# float_binary = ''

# if int_part == 0:
#     print('0')
# else:
#     while int_part > 0:
#         int_binary = str(int_part % 2) + int_binary
#         int_part = int_part // 2
# temp = float_part
# while temp > 0:
#     if len(float_binary) > 10:
#         break
    
#     temp = temp * 2
#     bit = int(temp)
#     if bit == 1:
#         float_binary += '1'
#         temp -= bit
#     else:
#         float_binary += '0'

# print(f"{int_binary}.{float_binary}")


# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# def short_form (string):
#     res = []
#     i = 0
#     while i < len(string) and string[i] == " ":
#         i += 1
#     if i < len(string):
#         res.append(string[i].upper())
#         i += 1
#     print(i)
#     while i < len(string):
#         print(i)
#         while i < len(string) and string[i] != " ":
#             i += 1
#             # print(i)
#         while i < len(string) and string[i] == " ":
#             i += 1
#             # print(i)
#         if i < len(string):
#             # print(i)
#             res.append(string[i].upper())

#     print("".join(res), i)

# short_form("  amisha  maurya   sdfgh dfghj       fghj        ")


# ------------------------------------------------------------------------------------------------------------------------------------------------- #

# def append_middle (string1, string2):
#     mid = len(string1) // 2
#     string3 = ''
#     for i in range (0, mid):
#         string3 += string1[i]
#     for j in range (0, len(string2)):
#         string3 += string2[j]
#     for k in range (mid, len(string1)):
#         string3 += string1[k]
    
#     print(string3)

# append_middle("campusx", "Data")


# ------------------------------------------------------------------------------------------------------------------------------------------------ #

# def rearrange (string):
#     L, res = [], ''
#     for i in range (len(string)):
#         if string[i] == string[i].lower():
#             L.append(string[i])
#     for j in range (len(string)):
#         if string[j] == string[j].upper():
#             L.append(string[j])
#     print("".join(L))

# rearrange("PyNaTive")

# -------------------------------------------------------------------------------------------------------------------------------------------------- #


# def symmetrical (string):
#     if len(string) % 2 == 0:
#         mid = (len(string) // 2)
#     if string[0:mid] == string[mid:len(string)]:
#         print("Symmetrical")
#     else:
#         print("Not symmetrical")

# symmetrical("khokho")


# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# def odd_one (string1, string2):
#     L1 = L2 = res = []
#     L1 = string1.split()
#     L2 = string2.split()
    
#     for k in L1:
#         if k not in L2:
#             res.append(k)
#     for l in L2:
#         if l not in L1:
#             res.append(l)
    
#     print(" ".join(res))

# a = "Apple Banana Mango"
# b = "Mango Kiwi Apple"
# odd_one(a, b)

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# def reverse_word (string):
#     L, res = [], ''
#     L = string.split()
#     for i in range (len(L)-1, -1, -1):
#         res += L[i] + ' '
#     print(res)

# a = "My Name is Amit"
# print(a)
# reverse_word("My Name is Amit")

# -------------------------------------------------------------------------------------------------------------------------------------------------- #


# def remove_duplicates (string):
#     L1, res = [], []
#     L1.extend(string)
#     print(L1)
#     for i in L1:
#         if i not in res:
#             res.append(i)
#     print(res)

# remove_duplicates("23444444")



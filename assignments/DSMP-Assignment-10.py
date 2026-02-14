# def get_final_line (filename):
#     with open (filename,'r') as f:
#         data = f.readline()
#         last_line = data
#         while True:
#             if data == '':
#                 break
#             else:
#                 last_line = data
#                 data = f.readline()
#         print(last_line)

# get_final_line(r'C:\Users\Amit Maurya\Desktop\DSMP Questions\file-handling\demo2.txt')

# ------------------------------------------------------------------------------------------------------------------------------------------------- #

# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\file-handling\sample.txt','r') as f:
#     count = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
#     data = f.readlines()
#     for i in data:
#         for j in i:
#             if j.lower() in ['a','e','i','o','u']:
#                 count[j.lower()] += 1
    
#     print(count)

# ------------------------------------------------------------------------------------------------------------------------------------------- #

# L = [1,2,3,4,5,6,7,8,9,10]

# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\file-handling\multiply-sum.txt','w') as f:
#     for i in range (0,len(L),2):
#         f.write(f"{L[i]}    {L[i+1]}\n")

# temp = [L[i]*L[i+1] for i in range(0,len(L),2)]
# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\file-handling\multiply-sum.txt','w') as f:
#     for i in range (0,len(L),2):
#         f.write(f"{L[i]}    {L[i+1]}    {L[i]*L[i+1]}\n")
#     f.write(f'Total:    {sum(temp)}')

# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\file-handling\multiply-sum.txt','r') as f:
#     print(f.read())

# ----------------------------------------------------------------------------------------------------------------------------------------- #

# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\file-handling\reverse1.txt','w') as f1:
#     # f.write('Amit is a Programmer\nHe wants to become a Data Scientists')
#     f1.write("abc def\nghi jkl")

# f = open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\file-handling\reverse1.txt','r')
# data = f.readline()

# processed_data = []
# while True:
#     if data != '':
#         temp = []
#         for word in data:
#             for char in word:
#                 if char != '\n':
#                     temp.append(char)
#         reverse_list = ''.join(i for i in temp[::-1])
#         processed_data.append(reverse_list + '\n')
#     else:
#         break
#     data = f.readline()
# f.close()
# print(processed_data)

# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\file-handling\reverse2.txt','w') as f4:
#     f4.writelines(processed_data)


#                                                       OR                                                          #
# data = readlines()
# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\file-handling\reverse1.txt','r') as f:
#     data = f.readlines()
# print(data)
# processed_data = []
# for word in data:
#     words = word.split()
#     print(words)
#     reverse_letters = ' '.join(i[::-1] for i in reversed(words))
#     processed_data.append(reverse_letters + '\n')
#     # print(processed_data)

# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\file-handling\reverse2.txt','w') as f4:
#     f4.writelines(processed_data)


#                                                       OR                                                          #

# processed_data = []
# while True:
#     if data != '':
#         # for line in data:
#         words = data.split()
#         # print(words)
#         reversed_list = ' '.join(word[::-1] for word in words[::-1])
#         processed_data.append(reversed_list)
#         # print(reversed_list)
#         processed_data.append('\n')
#     else:
#         break
#     data = f.readline()

# # print(processed_data)

# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\file-handling\reverse1.txt','w') as f:
#     f.writelines(processed_data)


# ----------------------------------------------------------------------------------------------------------------------------------------- #

# Mine
# file_path = r'C:\Users\Amit Maurya\Desktop\DSMP Questions\file-handling\frequency-of-words.txt'
# with open (file_path,'r') as f:
#     dic = {'alice':0, 'wonder':0, 'natural':0}
#     word_list = ['alice', 'wonder', 'natural']
#     data = f.readline()
#     counter = 0
#     while counter < 2:
#         if data != '':
#             line = data.split()
#             for i in line:
#                 if i.lower() in word_list:
#                     dic[i.lower()] += 1
#         else:
#             counter += 1
#         data = f.readline()
#     print(dic)


# file_path = r'C:\Users\Amit Maurya\Desktop\DSMP Questions\file-handling\frequency-of-words.txt'
# with open(file_path, 'r') as f:
#     dic = {'alice': 0, 'wonder': 0, 'natural': 0}
#     word_list = ['alice', 'wonder', 'natural']
#     for line in f:
#         words = line.split()
#         for word in words:
#             # Remove punctuation
#             word = word.lower().strip(".,:;!?()[]`'-\"")
#             if word in word_list:
#                 dic[word] += 1
#     print(dic)


# s = """ I shall be late!'  (when she thought it over afterwards, it occurred to her that she ought to have wondered at this,
#           but at the time it all seemed q,uite natural); but """
# temp = s.split()
# print(temp)
# punctuations = ".,:;''()"
# for word in temp:
#     word = word.lower()
#     #cleaned_word = ''.join(i for i in word if i not in punctuations)
#     cleaned_word = word.strip(".,:;''()")
#     print(cleaned_word)

# --------------------------------------------------------------------------------------------------------------------------------------- #

# def gcd (num1, num2):
#     return gcd2(min(num1, num2), num1, num2)

# def gcd2 (counter, num1, num2):
#     if counter == 0:
#         return 0
#     else:
#         if (num1 % counter == 0) and (num2 % counter == 0):
#             return counter
#         else:
#             print(0)
#             return gcd2(counter-1, num1, num2)
    
# print(gcd(16,24))

# ----------------------------------------------------------------------------------------------------------------------------------------- #
# counter = 1
# def length_string (string):
#     global counter
#     if string[0] == '':
#         return 0
#     if len(string) == 1:
#         return counter
#     else:
#         counter = counter + 1
#         return length_string(string[:-1])
# print(length_string(" Amit"))


# def length_string (string):
#     if string == '':
#         return 0
#     else:
#         return 1 + length_string(string[:-1])
# print(length_string(" Amit"))

# ----------------------------------------------------------------------------------------------------------------------------------------- #
# # Wrong Approach
# def gcd (a, b):
#     print(a, b)
#     if (max(a, b) % min(a, b)) == 0:
#         return min(a, b)
#     else:
#         return gcd((min(a, b) // 2), max(a, b))
# print(int(gcd(26, 36)))

# # Right Approach
# def gcd(a, b):
#     print(a, b)
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
# print(gcd(48, 18))


# # Correct but inefficient code
# a, b = 48, 18
# def gcd(a, b, counter):
#     print(a, b, counter)
#     if (a%counter == 0) and (b%counter == 0):
#         return counter
#     else:
#         counter -= 1
#         return gcd (a, b, counter)
# print(gcd(a, b, min(a, b)))

# ------------------------------------------------------------------------------------------------------------------------------------------------- #

# def string_distance (s1, s2):
#     if len(s1) == 0:
#         return len(s2)
#     if len(s2) == 0:
#         return len(s1)
    
#     if s1[0] == s2[0]:
#         return string_distance(s1[1:], s2[1:])
    
#     insert = string_distance(s1[:], s2[1:])
#     delete = string_distance(s1[1:], s2[:])
#     replace = string_distance(s1[1:], s2[1:])

#     return 1 + min(insert, delete, replace)

# print(string_distance("kitten", "sitting"))

# ----------------------------------------------------- #

# def string_distance(s1, s2, memo):
#     # Use a tuple of (s1, s2) as the key for memoization
#     if (s1, s2) in memo:
#         # print(memo)
#         return memo[(s1, s2)]
    
#     # Base cases
#     if len(s1) == 0:
#         return len(s2)
#     if len(s2) == 0:
#         return len(s1)
    
#     # If the first characters match, move to the next characters
#     if s1[0] == s2[0]:
#         result = string_distance(s1[1:], s2[1:], memo)
#     else:
#         # Compute the cost of insertion, deletion, and replacement
#         insert = string_distance(s1, s2[1:], memo)
#         delete = string_distance(s1[1:], s2, memo)
#         replace = string_distance(s1[1:], s2[1:], memo)
#         result = 1 + min(insert, delete, replace)
    
#     # Store the result in the memo dictionary
#     memo[(s1, s2)] = result
#     return result

# memo = {}
# print(string_distance("kitten", "sitting", memo))
# # print(memo)

# ------------------------------------------------------------------------------------------------------------------------------------------------- #

# def fibo (n, memo):
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
#         return memo[n]
    
# memo = {0:1,1:1}
# print(fibo(48, memo))
# print(memo)
# ------------------------------------------------------------------------------------------------------------------------------------------------- #

# def run_length_comperhension (L, d):
#     if len(L) == 0:
#         return 0
    
#     if L[0] not in d:
#         d[L[0]] = 1
#         return run_length_comperhension(L[1:], d)
    
#     if L[0] in d:
#         d[L[0]] += 1
#         result = run_length_comperhension(L[1:], d)
#         return d

# d = {}
# print(run_length_comperhension(["A", "A", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"], d))
# ---------------------------------------------------------------- #

# def run_length_comprehension (L, temp=None, d=None):
#     if temp == None:
#         temp = []
#     if d == None:
#         d = {}

#     if len(L) == 0:
#         return temp
    
#     if L[0] not in d:
#         d[L[0]] = 1
#         return run_length_comprehension(L[1:], temp=temp, d=d)
    
#     if L[0] in d:
#         d[L[0]] += 1
#         if len(L) > 1 and L[0] == L[1]:
#             run_length_comprehension(L[1:], temp=temp, d=d)
#         else:
#             run_length_comprehension(L[1:], temp=temp, d=None)
#         temp.extend(item for pair in d.items() for item in pair)
#     return temp

# print(run_length_comprehension(["A", "A", "B", "B", "B", "A", "B", "B"]))

# ---------------------------------------------------------------- #

# def run_length_comprehension (L, temp=None, current=None, count=None):
#     if temp == None:
#         temp = []

#     if len(L) == 0:
#         if current != None:
#             temp.append(current)
#             temp.append(count)
#         return temp

#     if current == None:
#         current = L[0]
#         count = 1
#         return run_length_comprehension(L[1:], temp=temp, current=current, count=count)
    
#     elif current == L[0]:
#         count += 1
#     else:
#         temp.append(current)
#         temp.append(count)
#         current = L[0]
#         count = 1
#     return run_length_comprehension(L[1:], temp=temp, current=current, count=count)

# print(run_length_comprehension(["A", "A", "B", "B", "B", "A", "B", "B", "Z"]))

# ------------------------------------------------- #

# def run_length_comprehension (L):
#     if len(L) == 0:
#         return []
    
#     count = 1
#     while count < len(L) and L[count] == L[0]:
#         count += 1
    
#     return [L[count-1],count] + run_length_comprehension(L[count:])

# print(run_length_comprehension(["A", "A", "B", "B", "B", "A", "B", "B", "Z"]))

# -------------------------------------------------- #


# def run_length_comprehension (L, temp=None):
#     if len(L) == 0:
#         return temp
    
#     if temp == None:
#         temp = []

#     def cout_consecutive (L, count=0):
#         if count < len(L) and L[count] == L[0]:
#             count += 1
#             return cout_consecutive(L, count=count)
        
#         return count
    
#     no_of_char = cout_consecutive(L, count=0)
#     temp.append(L[0])
#     temp.append(no_of_char)
#     return run_length_comprehension (L[no_of_char:], temp=temp)

# print(run_length_comprehension(["A", "A", "A", "A", "A", "B", "B", "B", "A", "B", "B", "Z"]))

# ------------------------------------------------------------------------------------------------------------------------------------------------- #

# def binary_to_decimal (num1, num2):
# 	n1, n2, add = 0, 0, 0
# 	for i in range (len(num1)):
# 		if num1[i]=='1':
# 			n1 += (2**i)
		
# 	for j in range (len(num2)):
# 		if num2[j]=='1':
# 			n2 += (2**j)
# 	return decimal_to_binary(n1, n2)

# def decimal_to_binary (n1, n2):
# 	add = n1 + n2
# 	res = ''
# 	while add > 0:
# 		rem = add % 2
# 		res = str(rem) + res
# 		add //= 2
# 	return res

# num1 = input("Enter the 1st Binary Number ")[::-1]
# num2 = input("Enter the 2nd Binary Number: ")[::-1]
# print(binary_to_decimal(num1, num2))

# -------------------------------------------------------
# Only conversion of decimal to binary

def decimal_to_binary (n, bi=None):
    if bi == None:
        bi = ''

    if n == 0:
        return bi
    
    else:
        rem = n % 2
        bi = str(rem) + bi

    return decimal_to_binary(n//2, bi=bi)

print(decimal_to_binary(20))


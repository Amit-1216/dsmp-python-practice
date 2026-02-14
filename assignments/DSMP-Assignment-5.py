# def remove_duplicates (L):
#     temp = []
#     for i in range (len(L)):
#         if L[i] not in temp:
#             temp.append(L[i])
    
#     print(temp)

# remove_duplicates([1,1,22,33,44,55,66,66,66])

# ------------------------------------------------------------------------------------------------------------------------------------------ #

# def sort_string (L):
#     for i in range (len(L)-1):
#         flag = True
#         for j in range (len(L)-i-1):
#             if L[j] > L[j+1]:
#                 L[j], L[j+1] = L[j+1], L[j]
#                 flag = False
#         if flag:
#             break

# def transform (string):
#     temp = string.split('-')
#     sort_string(temp)
#     res = '-'.join(temp)
#     print(res)

# transform("Amit-Maurya-Ashok")

# ------------------------------------------------------------------------------------------------------------------------------------------ #

# def upper_lower (string):
#     upper_count, lower_count = 0, 0
#     for i in range (len(string)-1):
#         if string[i] == string[i].upper() and string[i] != ' ':
#             upper_count += 1
#         elif string[i] == string[i].lower() and string[i] != ' ':
#             lower_count += 1
    
#     print("Upper Count:",upper_count)
#     print("Lower Count:",lower_count)

# upper_lower('CampusX is an Online Mentorship Program fOr EnginEering studentS.')

# ------------------------------------------------------------------------------------------------------------------------------------------ #

# def perfect (num):
#     temp = num
#     for i in range (1, num):
#         if num%i == 0:
#             temp += i
#     if temp//2 == num:
#         print("Perfect")
#     else:
#         print("Not Perfect")   
# perfect(8128)

# ------------------------------------------------------------------------------------------------------------------------------------------ #

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}

# def concatenate (*args):
#     dic = {}
#     for i in args:
#         dic.update(i)
#     print(dic)

# concatenate(dic1,dic2,dic3)

# ------------------------------------------------------------------------------------------------------------------------------------------ #

# def No_of_occurence (string):
#     count = 0
#     temp = []
#     L = string.split()
#     for i in range (len(L)):
#         if L[i] in L[i+1:]:
#             count += 1
#             temp.append(L[i])
#     print(temp, count)

# No_of_occurence("hello how are you i am fine thank you you are")


# ----------------------------------------------------------------------------------------------------------------------------------------------- #


# def most_frequent_word (string):
#     count = 1
#     n = 1
#     L = string.split()
#     # print(L)
#     temp = {}

#     for i in L:
#         if i in temp:
#             temp[i] += 1
#         else:
#             temp[i] = count
#     # print(temp)

#     max_val = 0
#     most_common_word = None

#     for key, value in temp.items():
#         if value > max_val:
#             max_val = value
#             most_common_word = key
    
#     print(most_common_word, "->" ,max_val)

# most_frequent_word("hello you how are you i am fine thank you")

# ----------------------------------------------------------------------------------------------------------------------------------------------- #


# def histogram (L):
#     min_val = min(L)
#     if min_val % 10 != 0:
#         for i in range (min_val, -1, -1):
#             if i % 10 == 0:
#                 break
#         min_range = i
#     else:
#         min_range = min_val

#     max_val = max(L)
#     max_range = max_val if max_val % 10 == 0 else (((max_val // 10) + 1) * 10)

#     dic = {}
#     counter, temp = 0, (max_range - 9)
#     for j in range (max_range//10):
#         dic[f"{min_range+counter}-{(max_range - temp)}"] = []
#         counter += 10
#         temp -= 10
#     # print(dic)

#     for num in L:
#         for bin_range in dic:
#             str_start_range = str_end_range = bin_range.split('-')
#             start_range = int(min(str_start_range))
#             end_range = int(max(str_end_range))
#             if start_range <= num <= end_range:
#                 dic[bin_range].append(num)
#                 break
#     print(dic)

# histogram([2,12,16,25,36,44,51])


# ------------------------------------------------------------------------------------------------------------------------------------------------------- #


# def Euclidean_distance (List, query):
#     temp = []
#     for i in range (len(List)):
#         x = ((List[i][0] - query[0][0]) ** 2)
#         y = ((List[i][1] - query[0][1]) ** 2)
#         temp.append(x+y)
    
#     min_val = min(temp)
#     min_distance = temp.index(min_val)
#     print(List[min_distance])

# Euclidean_distance([(1,2),(4,6),(7,8),(2,1)], [(3, 3)])
# Euclidean_distance([(1,1),(2,2),(3,3),(4,4)], [(0, 4)])


# ------------------------------------------------------------------------------------------------------------------------------------------------------- #

# def bow(sentences):
#     # Tokenize and normalize sentences
#     tokenized_sentences = [sentence.lower().split() for sentence in sentences]

#     # Create a vocabulary set
#     vocab_set = set()
#     for words in tokenized_sentences:
#         for word in words:
#             vocab_set.add(word)

#     # Convert vocabulary set to a list to maintain consistent ordering
#     vocab_list = list(vocab_set)
    
#     # Create a vector for each sentence
#     vectors = []
#     for sentence in tokenized_sentences:  # Using tokenized_sentences
#         temp = []
#         for word in vocab_list:
#             temp.append(sentence.count(word))  # Correctly counting words in tokenized sentences
#         vectors.append(temp)

#     # Print the vectors
#     for vector in vectors:
#         print(vector)

# # Example usage
# bow([
#     "Hello how are you",
#     "I was waiting for your call",
#     "Where do you work",
#     "Lets meet someday",
#     "Hope you are fine"
# ])


# -------------------------------------------------------------------------------------------------------------------------------------------------------- #





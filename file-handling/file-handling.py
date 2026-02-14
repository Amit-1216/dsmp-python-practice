# f = open(r'C:\Users\Amit Maurya\Desktop\DSMP Questions\example.txt','r')
# L = ['hello\n','hii\n','How are you?\n',"I'm fine"]
# f = open(r'sample.txt','w')
# f.writelines(L)
# f.close()
# f = open('sample.txt','r')

# while True:
#     line = f.readline()
#     if line == '':
#         break
#     else:
#         print(line)
# f.close()

# #while f.readline() != '':
#  #   print(f.readline())
# #f.close()

# ------------------------------------------------------------------------------------------------------------------------------------------------- #

# f = open('sample.txt','r')
# print(f.read())
# line = f.readline()
# # while True:
# while line:        # or while line != '':
#     # if line == '':
#     #     break
#     # else:
#     print(line)
#     line = f.readline()
# f.close()

# ----------------------------------------------------------------------------------------------------------------------------------------------------- #

# with open('sample.txt','r') as f:
#     print(f.read(12))

# big_data = ["Amit" for i in range (100)]
# with open('sample.txt','w') as f:
#     f.writelines(big_data)

# with open('sample.txt','r') as f:
#     chunk_val = 10
#     chunk_data = f.readline(chunk_val)
#     while len(chunk_data) > 0:
#         print(chunk_data, end=' | ')
#         chunk_data = f.readline(chunk_val)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------- #
# L = ['hello\n','hii\n','How are you?\n',"I'm fine"]
# with open('sample.txt','w') as f:
#     f.writelines(L)
#     f.write("Amit")
#     f.seek(2)
#     f.write("Maurya")

# with open('sample.txt','r') as f:
#     print(f.read())

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- #

# with open(r'C:\Users\Amit Maurya\Desktop\DSMP Questions\puppies.jpeg','rb') as rf:
#     with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\puppies2.jpeg','wb') as wf:
#         wf.write(rf.read())

# -------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Serialization
# import json
# # L = [1,2,3,4,5]
# L = (1,2,3,4,5)
# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\demo.txt','w') as f:
#     json.dump(L,f)

# d = {
#     'name' : 'Amit',
#     'roll No.' : 30,
#     'std' : 'SY'
# }

# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\demo2.txt','w') as demo2:
#     json.dump(d,demo2,indent=4)

# Deserialization
# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\demo.txt','r') as f:
#     print(json.load(f))

# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\demo2.txt','r') as demo2:
#     d = json.load(demo2)
#     print(d, type(d))


# -------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# class Person:
#     def __init__ (self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

# obj = Person('Amit', 20, 'Male')

# def  structure (obj):
#     if isinstance (obj, Person):
#         return f"{obj.name} -> {obj.age} -> {obj.gender}"

# import json
# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\demo2.txt','w') as f:
#     json.dump(obj, f, default=structure)

# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\demo2.txt','r') as f:
#     print(json.load(f))

# ----------------------------------------------------------------------------------------------------------------------------------------------------------- #

# class Person:
#     def __init__ (self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

# obj = Person('Amit', 20, 'Male')

# def  structure (obj):
#     if isinstance (obj, Person):
#         # return {'Name':obj.name, 'Age':obj.age, 'Gender':obj.gender}
#         # return [obj.name, obj.age, obj.gender]
#         return (obj.name, obj.age, obj.gender)

# import json
# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\demo2.txt','w') as f:
#     json.dump(obj, f, default=structure)

# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\demo2.txt','r') as f:
#     print(json.load(f))

# ----------------------------------------------------------------------------------------------------------------------------------------------------- #

# Pickling
# import pickle
# # L = [11,22,33,44,55]

# class Person:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age
    
#     def display (self):
#         return f"{self.name} -> {self.age}"

# p = Person('Amit', 20)

# with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\temp.pkl', 'wb') as f:
#     pickle.dump(p,f)

# with open('C:\\Users\\Amit Maurya\\Desktop\\DSMP Questions\\temp.pkl', 'rb') as f:
#     data = pickle.load(f)
#     print(data)

# print(data.display())

# --------------------------------------------------------------------------------------------------------------------------------------------------------- #

import json

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

def structure (obj):
    # return f"{obj.name} -> {obj.age}"
    return obj

p = Person('Amit', 20)

with open (r'C:\Users\Amit Maurya\Desktop\DSMP Questions\temp2.json', 'w') as f:
    json.dump(p,f,default=structure)

with open('C:\\Users\\Amit Maurya\\Desktop\\DSMP Questions\\temp2.json', 'r') as f:
    data = json.load(f)
    print(data)
    print(type(data))

print(data.name)




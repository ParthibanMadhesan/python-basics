# thislist=["mango","apple","orange","kiwi"]
# print(thislist)

# #ordered
# print(thislist)


# #changeableb and duplicate allowed

# thislist1 = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist1)

# print(len(thislist1))

# list1 = ["abc", 34, True, 40, "male"]
# print(list1)

# #list()constructor

# list2=list(("apple","banana","chery"))
# print(list2)

# #access list item

# print(list2[1])

# #negative indexing
# print(list2[-1])
# print(list2[1:])
# print(list2[-3:-1])

# #CHECK IF element is exist

# if "apple" in list2:
#     print("yes apple is present")
# else:
#     print("not present")


# #change list of items

# list2[1]="blackcurrent"

# print(list2)

# # change the range of items and values

# list2[1:2]=["watermelon","grapes"]
# print(list2)

# #insert items
# list2.insert(1,"kiwi")
# print(list2)

# #add listitem

# list2.append("mango")
# print(list2)

# #extend the list
# vegetable=["carrot","beans","potato"]
# list2.extend(vegetable)
# print(list2)

# # remove list items
# list2.remove("carrot")
# print(list2)

# list2.pop()
# print(list2)

# list2.pop(1)
# print(list2)
# print("----------------------")
# #delete the list

# del list2[1]
# print(list2)

# list2.clear()
# print(list2)

# #looping

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)

# for i in range(len(thislist)):
#     print(thislist[i])


# #using while loop

# thislist1= ["apple", "banana", "cherry"]

# i=0
# while i<len(thislist1):
#     print(thislist1[i])
#     i=i+1


# print("------------------")
# [print(x) for x in thislist1]

# #list Comphrension

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newList=[]

# for x in fruits:
#     if "a" in x:
#         newList.append(x)
# print(newList)


# print("------------------")

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# print("------------------")

# newlist = [x for x in fruits if x != "apple"]

# print(newlist)

# print("------------------")
# newlist = [x for x in range(15)]

# print(newlist)

# print("-------------------")


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[x if x!="banana" else "orange" for x in fruits]
# print(newlist)

# newlist=[x.upper() for x in fruits]
# print(newlist )

# #List objects have a sort() method that will sort the list alphanumerically, 

# newlist.sort(reverse=True)
# print(newlist)


# print("-------------------")


# def myfunc(n):
#   return abs(n - 50)

# thislist = [79, 50, 65, 82, 33]
# thislist.sort(key = myfunc)
# print(thislist)

class User:
    def __init__(self,id,username,password):
        self.id=id
        self.username=username
        self.password=password


users=[]

users.append(User(id=1,username='sathya',password='1234')) 
users.append(User(id=2,username='partha',password='123')) 

for user in users:
   
    print(f"ID: {user.id}, Username: {user.username}, Password: {user.password}")

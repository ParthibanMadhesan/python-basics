thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
print(type(thisset))

thisset = set(("apple", "banana", "cherry"))
print(thisset)

for x in thisset:
    print(x)

print("banana" in thisset)

thisset.add("goa")
print(thisset)

mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

set2 = {1, 2, 3}

set3=thisset.union(set2)
print(set3)

set1={"i","a","s"}
set1.update(set2)
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.intersection(y)
print(z)
print("----------------------")
x.intersection_update(y)
print(z)
print("----------------------")



x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z=x.difference(y)
print(z)
print("--------------------------")
z=x-y
print(z)
print("------------------------")
x.difference_update(y)
print(x)

print("----------------------")


x1 = {"apple", "banana", "cherry"}
y1= {"google", "microsoft", "apple"}

z1=x1.symmetric_difference(y1)
print(z1)
x1.symmetric_difference_update(y1)
print(x1)

z1=x1^y1
print(x1)

print("----------------------")


x1 = {"apple", "banana", "cherry"}
y1= {"google", "microsoft", "mango"}

z=x1.isdisjoint(y1)
print(z)

print("------------------")

alpha= {1,2,3,"a","b","c"}
beta={"a","b","c"}
gamma=alpha.issuperset(beta)
print(gamma)
gamma=alpha>=beta
print(gamma)
print("______________________")

gamma=beta.issubset(alpha)
print(gamma)
gamma=beta<=alpha
print(gamma)

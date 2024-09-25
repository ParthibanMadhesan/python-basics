thisdict={
    "brand":"ford",
    "model":"mustard",
    "year":1964
}
print(thisdict)

print("---------------")

thisdict["year"]=1999
print(thisdict)
print(len(thisdict))

print("-------------------")

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)
print(type(thisdict))
print("-------------------")

thisdict= dict(name="john",country="norway")
print(thisdict)

x=thisdict["country"]
print(x)
print("-------------------")
print(thisdict.get("name"))
print(thisdict.keys())
print(thisdict.values())

if "name" in thisdict:
    print("yes name is one of the key in thisdict")
else:
   print("is not there")  

print("-------------------")

thisdict.update({"name":"michal"})
print(thisdict)

print(thisdict.items())

print("--------------------")
for x in thisdict:
  print(thisdict[x])

print("--------------")
for x in thisdict.values():
   print(x)
   
print("------------------")
for x,y in thisdict.items():
   print(x,y)

print("---------------------------")
mydict=thisdict.copy()
print(mydict)


print("-----------------------")

myfamily={
   
   "family1":{
      "name":"kanaga",
      "age":22
   },
   "family2": {
      "name":"partha",
      "age" :24
   },
   "family3":{
      "name":"swetha",
      "age":25
   }
}

print(myfamily)

print(myfamily["family2"]["name"])

for x,obj in myfamily.items():
   print(x)
   for y in obj:
      print(y+":",obj[y])


x={"key1","key2","key3"}
thisdict=dict.fromkeys(x)
print(thisdict)

y=0
thisdict=dict.fromkeys(x,y)
print(thisdict)
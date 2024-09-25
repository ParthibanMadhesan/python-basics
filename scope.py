def myfunc():
    x=300
    print(x)
myfunc()

print("------------------")

def myfunct():
    x=200
    def myfunct1():
        print(x)
    myfunct1()
myfunct()

print(";----------------------")

a=100
def newfunc():
    print(a)

newfunc()
print(a)

print("--------------------------")

#module 

import mymodule

mymodule.myfunct("harshini")

from mymodule import person1

a=mymodule.person1["age"]
print(a)


import mymodule as md
a=md.person1["name"]
print(a)


import platform

x=platform.system()
print(x)

x=dir(platform)
print(x)


#dates and times
import datetime

x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))


x=datetime.datetime(2020,5,17)
print(x)
print(x.strftime("%B"))
print(x.strftime("%V"))


import math
x=min(5,10,25)
y=max(10,25,85)
print(x)
print(y)

z=abs(-76)
print(z)

w=pow(2,3)
print(w)

p=math.sqrt(20)
print(p)
q=math.ceil(7.2)
r=math.floor(7.8)
print(q)
print(r)
s=math.pi
print(s)


#json

import json

print(json.dumps(None))

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))




x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
y=json.dumps(x,indent=4)
print(y)
print("------------------")
y=json.dumps(x,indent=4,separators=(".","="))
print(y)
print("------------------")
y=json.dumps(x,indent=4,sort_keys=True)
print(y)



#regex specify the search pattern

import re
txt="the rain in spain"

x=(re.search("^the.*spain$",txt))

if x:
    print("we have match")
else:
    print("no match")


# print("------------------")
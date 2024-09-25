class MyClass:
    x=5
    print(x)

print(MyClass)

p1=MyClass()
print(p1.x)


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
         return f"{self.name},{self.age}"
    
p1=Person("john",22)
print(p1)


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("i am "+self.name,self.age)
        
p1=Person("john",22)
p1.myfunc()




# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def myfunc(self):
#         print("i am "+self.name)
        
# p1=Person("john",22)
# del p1.age
# del p1
# p1.myfunc()


print("-----------------------------------")


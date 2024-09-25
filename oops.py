#inheritance

class Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age

    def printname(self):
        print("i am "+self.name ,"my age",self.age)
class Student(Person):
    def __init__(self, name, age):
        Person.__init__(self,name, age)

obj=Student("swetha",23)
obj.printname()



class A:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printName(self):
        print(self.fname,self.lname)

class B(A):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.year=year
    def welcome(self):
        print(self.fname,self.lname,self.year)

obj=B("shruthi","kesavan",2000)
obj.printName()
obj.welcome()


#iterator methods-->iter,next

mytuple=("apple","banana","grapes")

myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))


mystr="grapes"
myit1=iter(mystr)
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))

print("-----------------------------")

class Numbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass=Numbers()
myit=iter(myclass)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print("-----------------------------")

class Numbers:
    def __iter__(self):
         self.a=1
         return self
    def __next__(self):

     if self.a<=20:
        x=self.a
        self.a+=1
        return x
     else:
         raise StopIteration
myclass=Numbers()
myit=iter(myclass)

for x in myit:
    print(x)


print("-----------------------------")

#polumorphism

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("move!")
class Boat:
     def __init__(self,brand,model):
        self.brand=brand
        self.model=model

     def move(self):
         print("sail")
class plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("fly")

myCar=Car("Ford","mustang")
myBoat=Boat("ibiza","towering 20")
myPlane=plane("boeing","747")

for x in (myCar,myBoat,myPlane):
    # print(x.brand)
    # print(x.model)
    x.move()

#polymorphism (inheriting class)

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
         print("move")

class Car(Vehicle):
   pass
class Boat(Vehicle):
    
     def move(self):
         print("sail")
class plane(Vehicle):
    
    def move(self):
        print("fly")

myCar=Car("Ford","mustang")
myBoat=Boat("ibiza","towering 20")
myPlane=plane("boeing","747")

for x in (myCar,myBoat,myPlane):
    print(x.brand)
    print(x.model)
    x.move()


class Character:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

class Wizard(Character):
    def __init__(self, health, attack, magic):
        super().__init__(health, attack)
        self.magic = magic
    
class Warrior(Character):
    def __init__(self, health, attack, magic):
        super().__init__(health, attack,magic)
        
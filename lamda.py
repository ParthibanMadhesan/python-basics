
#lambda function 

x=lambda a:a+10
print(x(5))

y=lambda a,b:a+b
print(y(5,3))

x= lambda a,b,c:a*b*c
print(x(2,4,7))


def myfunct(n):
    return lambda a:a*n
mydoubler=myfunct(10)

print(mydoubler(10))


def myfunction(n):
    return lambda a:a*n

mydou=myfunct(5)
mytri=myfunct(2)

print(mydou(5))
print(mytri(3))

cars=["ford","bmw","volvo"]
print(cars)


cars=["ford","bmw","volvo"]
x=cars[0]
print(x)

cars[0]="audi"
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

for x in cars:
    print(x)

cars1=["toyoto","fortuner","ferrari"]


cars.append(cars1)
print(cars)
print(cars1)

cars.extend(cars1)
print(cars)
print(cars1)

#cars.pop(3)
print(cars)

cars.remove("toyoto")
print(cars)

x=cars.index("ferrari")
print(x)


def myfuncc(e):
    return len(e)


cars1=["toyoto","fortuner","ferrari"]
cars1.sort(key=myfuncc)
print(cars1)
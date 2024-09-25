x = ("apple", "banana", "cherry")
y=list(x)
y[1]="orange"
x=tuple(y)
print(x)

y=list(x)
y.append("kiwi")
x=tuple(y)
print(x)

(green,yellow,*red)=x
print(green)
print(yellow)
print(red)
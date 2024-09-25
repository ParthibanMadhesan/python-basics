a=10
b=20
print("a")if a>b else print("b")

a=330
b=330

print("A")if a>b else print("=") if a==b  else print("b")

#looping

#while loop

i=0
while i<6:
   i=i+1
   if i==3:
     continue
   print(i)


   print("------------------")

i=1
while i<6:
   print(i)
   i=i+1
else:
   print("completed loop")

   print("------------------")

a = 2
b = 5
print("YES") if a==b  else print("NO")


fruits = ["apple", "banana", "cherry"]

for x in fruits:

   if x=="banana":
       continue
   print(x)



print("------------------")


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


print("------------------")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
   for y in fruits:
     print(x,y)

print("------------------")

for i in [0,1,2,3]:
   print(i)
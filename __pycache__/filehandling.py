f=open("/home/nxgen-02/Documents/demo/demofile.txt","r")
print(f.readline())
print(f.readline())

f=open("/home/nxgen-02/Documents/demo/demofile.txt","a")
f.write("hello google i need your help")
f.close

f=open("/home/nxgen-02/Documents/demo/demofile.txt","r")
for x in f:
  print(x)

f=open("/home/nxgen-02/Documents/demo/demofile.txt","w")
f.write("already i was worked in java developer")

f=open("/home/nxgen-02/Documents/demo/demofile.txt","r")
print(f.read())

f.close()

import os
#os.remove("/home/nxgen-02/Documents/demo/demofile.txt")

# if os.path.exists("/home/nxgen-02/Documents/demo/demofil.txt"):
#     os.remove("/home/nxgen-02/Documents/demo/demofile.txt")
# else:
#    print("the file doesn't exist")


os.rmdir("/home/nxgen-02/Documents/demo")

print("removed")
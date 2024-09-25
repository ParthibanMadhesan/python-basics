
try:
    print(x)
except NameError:
    print ("the name error")
except:
    print("something else wrong")
else:
    print("executed")
finally:
    print("always executed")
price=59
txt=f"the coin {price} rupee"
print(txt)

txt=f"the coin {price:.2f} rupee"
print(txt)

price=60
tax=15
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

fruit="mango"
txt = f"I love {fruit.upper()}"
print(txt)

def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

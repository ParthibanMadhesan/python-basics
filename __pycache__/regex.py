
import re

txt="i hate you so much 123"
x=re.findall("[a-m]",txt)
print(x)

x=re.findall("\d",txt)
print(x)

x=re.findall("h..e",txt)
print(x)

x=re.findall("^i",txt)
print(x)

x=re.findall("\Ai",txt)
print(x)

y=IndexError
print(y)
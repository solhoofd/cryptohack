from sage.all import *

a = Mod(2,5)
b = Mod(3,11)
c = Mod(5,17)

x = c.crt(b)
print(x.crt(a))


a = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

a = int(a, 16)
res = ""
t = a % 256
while t != 0:
  res = chr(t) + res
  a -= t
  a //= 256
  t = a % 256
print(res)


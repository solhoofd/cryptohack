a = 66528; b = 52920

def gcd(a, b):
  while b != 0:
    t = b
    b = a % b
    a = t
  return a

print(gcd(a, b))


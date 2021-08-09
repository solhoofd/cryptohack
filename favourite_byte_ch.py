from pwn import xor

def my_xor(a: bytes, b: bytes):
  r, o = (bytearray(a), b) if len(a) >= len(b) else (bytearray(b), a)
  for i in range(len(r)):
    r[i] ^= o[i%len(o)]
  return r

a = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
a = bytes.fromhex(a)

''' with my_xor
for x in range(256):
  x = bytes([x])
  print(my_xor(a, x))
  if b'crypto' in my_xor(a, x):
    res = my_xor(a, x)
    break
'''

for x in range(256):
  if b'crypto' in xor(a, x):
    res = xor(a, x)
    break

print(res.decode())


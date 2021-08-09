p = 26513; q = 32321

def ext_gcd(a, b):
  s = 0; old_s = 1
  r = b; old_r = a

  while r != 0:
    q = old_r // r
    (old_r, r) = (r, old_r - q * r)
    (old_s, s) = (s, old_s - q * s)

  if b != 0: t = (old_r - old_s * a) // b
  else: t = 0
  
  return (old_s, t)

u, v = ext_gcd(p, q)
print('crypto{{{},{}}}'.format(u,v))


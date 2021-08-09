from sage.all import *
from sage.rings.finite_rings.integer_mod import square_root_mod_prime as sqrt

with open('output1.txt', 'r') as f:
  a, p = f.read().split('\n', 1)
  a = int(a.split(' ')[-1])
  p = int(p.split(' ')[-1])
  
  a = Mod(a,p)
  print(sqrt(a))


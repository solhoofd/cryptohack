from sage.all import *

def gaussian_reduction(v, u):
  while True:
    if u.norm() < v.norm(): v, u = u, v
    m = floor(v.dot_product(u) / v.dot_product(v))
    if m == 0: break
    u = u - m*v
  return v, u

v = vector([846835985, 9834798552])
u = vector([87502093, 123094980])

v, u = gaussian_reduction(v, u)
print(v.dot_product(u))


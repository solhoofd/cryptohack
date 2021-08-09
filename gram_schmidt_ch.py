from sage.all import *

v1 = vector([4,1,3,-1])
v2 = vector([2,1,-3,4])
v3 = vector([1,0,-2,7])
v4 = vector([6,2,9,-5])

v = [v1, v2, v3, v4]
u = [None]*len(v)

u[0] = v[0]
for i in range(1, len(v)):
  u[i] = v[i]
  for j in range(i):
    t = v[i].dot_product(u[j]) / u[j].dot_product(u[j])
    u[i] -= t*u[j]

print(round(float(u[3][1]), 5))


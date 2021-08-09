from sage.all import *
from Crypto.Util.number import long_to_bytes
from math import sqrt, ceil

with open('output3.txt', 'r') as f:
  p, c = f.read().split('\n', 1)
pubk = [int(x) for x in p.lstrip('Public key: [').rstrip(']').split(', ')]
ct = int(c.split(' ')[2])
l = len(pubk)
#d = l / math.log(max(pubk), 2)
#print("density:", d)

N = ceil(sqrt(l) / 2)
L = matrix(ZZ, (2*matrix.identity(ZZ, l)).rows() + [vector(ZZ, [1 for x in range(l)])])
L_h = [[2*N*x] for x in pubk]
L_h.append([2*N*ct])
L = L.augment(matrix(L_h))

X = L.LLL()
for row in X:
  if row[-1] != 0: continue
  if not all([x==-1 or x==1 for x in row[:-1]]): continue
  row = vector([(-x+1)//2 for x in row])
  assert row[:-1].dot_product(vector(pubk)) == ct
  print(long_to_bytes(int(''.join([str(x) for x in reversed(row[:-1])]), 2)).decode())
  break


from math import sqrt

with open('output.txt', 'r') as f:
  p, ints = f.read().split('\n')[::2]
  p = int(p.split(' ')[-1])
  ints = [int(x) for x in ints.split(' ', 2)[-1][1:-1].split(', ')]

  for a in ints:
    if pow(a, (p-1)//2, p) == 1:
      break
  
  print(pow(a, (p+1)//4, p))


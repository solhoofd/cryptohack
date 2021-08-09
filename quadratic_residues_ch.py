p = 29
ints = [14, 6, 11]

res = []
for i in range(29):
  sq = i**2 % p
  if sq in ints:
    res.append(i)

print(min(res))


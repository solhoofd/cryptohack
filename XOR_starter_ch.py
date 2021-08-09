a = 'label'
b = 13
FLAG = 'crypto{{{}}}'

print(FLAG.format(''.join([chr(ord(x) ^ b) for x in a])))


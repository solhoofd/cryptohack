from pwn import xor

a = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

a = bytes.fromhex(a)

# here you see that the key is 'myXORke' + 'y'
#print(xor(a, b'crypto{' + (len(a)-8)*bytes([0]) + b'}'))

print(xor(a, b'myXORkey').decode())


from Crypto.Util.asn1 import DerSequence, DerBitString

with open('2048b-rsa-example-cert.der', 'rb') as f:
  a = f.read()
  d = DerSequence()
  a = d.decode(a)
  a = d.decode(a[0]) # main sequence
  a = d.decode(a[5]) # last element
  a = DerBitString().decode(a[1]) # bit string
  a = d.decode(a.value) # sequence in bit string
  print(a[0])
  

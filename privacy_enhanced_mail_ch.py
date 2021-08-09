import base64
from Crypto.Util.asn1 import DerSequence

with open("privacy_enhanced_mail.pem", "r") as f:
  a = f.read()
  a = a.lstrip('-----BEGIN RSA PRIVATE KEY-----\n')
  a = a.rstrip('\n-----END RSA PRIVATE KEY-----\n')
  a = base64.b64decode(a)
  a = DerSequence().decode(a)[:]
  print(a[3]) # privateExponent element in PKCS#1 format


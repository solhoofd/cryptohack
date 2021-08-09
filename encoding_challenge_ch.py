import telnetlib
import json
import base64
import codecs
from Crypto.Util.number import long_to_bytes

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

resp = json.loads(tn.read_until(b'\n').decode())
while "flag" not in resp:
  t = resp["type"]
  e = resp["encoded"]
  #print(resp)
  if t == "base64":
    d = base64.b64decode(e).decode()
  if t == "hex":
    d = bytes.fromhex(e).decode()
  if t == "rot13":
    d = codecs.decode(e, 'rot13')
  if t == "bigint":
    d = long_to_bytes(int(e, 16)).decode()
  if t == "utf-8":
    d = ''.join([chr(x) for x in e])
  to_send = {"decoded": d}
  #print("\t", to_send)
  tn.write(json.dumps(to_send).encode())
  resp = json.loads(tn.read_until(b'\n').decode())

print(resp["flag"])


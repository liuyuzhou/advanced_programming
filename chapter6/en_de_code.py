s = b'hello'
import binascii
h = binascii.b2a_hex(s)
print(f'base: {h}')
print(f'b2a hex: {binascii.a2b_hex(h)}')


import base64
h = base64.b16encode(s)
print(f'base: {h}')
print(f'b16 decode: {base64.b16decode(h)}')


h = base64.b16encode(s)
print(f'base: {h}')
print(f"decode: {h.decode('ascii')}")

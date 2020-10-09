import sys
print(f'sys file system encoding is: {sys.getfilesystemencoding()}')


with open('pytho\xf1o.txt', 'w') as f:
    f.write('hello world!')

import os
print(f"list dir: {os.listdir('.')}")

print(f"list dir: {os.listdir(b'.')}")

with open(b'python\xcc\x83o.txt') as f:
    print(f'read result: {f.read()}')
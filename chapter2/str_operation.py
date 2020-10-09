test_str = b'Hello World'
print(test_str[0: 5])
print(test_str.startswith(b'Hello'))
print(test_str.split())
print(test_str.replace(b'World', b'Python'))


test_list = bytearray(test_str)
print(test_list[0: 5])
print(test_list.startswith(b'Hello'))
print(test_list.split())
print(test_list.replace(b'World', b'Python'))


data = b'FOO:BAR,SPAM'
import re
# re.split('[:,]',data)
re.split(b'[:,]',data)


a = 'Hello World'
print(f'str result:{a[0]}')
print(f'str result:{a[1]}')

b = b'Hello World'
print(f'binary result:{b[0]}')
print(f'binary result:{b[1]}')


s = b'Hello World'
print(s)
print(s.decode('ascii'))


# print(b'{} {} {}'.format(b'ACME', 100, 490.1))
print(f"{b'ACME'} {100} {200.5}'")


print(f"{'ACME':10s} {100:10d} {200.5:10.2f}'".encode('ascii'))


with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')

import os
os.listdir('.')
os.listdir(b'.')

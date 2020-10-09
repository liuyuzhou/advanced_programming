# Read the entire file as a single byte string
with open('test.bin', 'rb') as f:
    data = f.read()

# Write binary data to a file
with open('test.bin', 'wb') as f:
    f.write(b'Hello World')


t = 'Hello World'
print(f'str object t[0] = {t[0]}')
for c in t:
    print(f'str value is: {c}')

b = b'Hello World'
print(f'binary object b[0] = {b[0]}')

for c in b:
    print(f'binary value is: {c}')


with open('test.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('test.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))


import array
num_list = array.array('i', [1, 3, 5, 7])
with open('test.bin','wb') as f:
    f.write(num_list)


import array
a_obj = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('test.bin', 'rb') as f:
    f.readinto(a_obj)

print(f'object of a is: {a_obj}')
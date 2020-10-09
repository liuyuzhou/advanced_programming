import os
import mmap

def memory_map(file_name, access=mmap.ACCESS_WRITE):
    size_val = os.path.getsize(file_name)
    fd = os.open(file_name, os.O_RDWR)
    return mmap.mmap(fd, size_val, access=access)


size = 1000000
with open('test_data', 'wb') as f:
    f.seek(size - 1)
    f.write(b'\x00')


m = memory_map('test_data')
print(f'the len of m is: {len(m)}')
print(f'm split: {m[0:10]}')
print(f'm[0] is: {m[0]}')
m[0:11] = b'Hello World'
print(f'close result: {m.close()}')

with open('test_data', 'rb') as f:
    print(f'read content: {f.read(11)}')


with memory_map('test_data') as m:
    print(f'obj len: {len(m)}')
    print(f'point content: {m[0:10]}')
print(m.closed)


# m = memory_map(file_name, mmap.ACCESS_READ)
#
#
# m = memory_map(file_name, mmap.ACCESS_COPY)


m = memory_map('test_data')
v = memoryview(m).cast('I')
v[0] = 7
print(f'point content from m is: {m[0:4]}')
m[0:4] = b'\x07\x01\x00\x00'
print(f'v[0] = {v[0]}')


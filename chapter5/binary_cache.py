import os.path

def read_into_buffer(file_name):
    buf = bytearray(os.path.getsize(file_name))
    with open(file_name, 'rb') as f:
        f.readinto(buf)
    return buf


with open('test_file.bin', 'wb') as f:
    f.write(b'Hello World')
buf_read = read_into_buffer('test_file.bin')
print(f'buf read is: {buf_read}')
buf_read[0:5] = b'Hello'
print(f'buf read is: {buf_read}')
with open('new_test_file.bin', 'wb') as f:
    f.write(buf_read)


# Size of each record (adjust value)
record_size = 32

buf_read = bytearray(record_size)
with open('test_file', 'rb') as f:
    while True:
        n = f.readinto(buf_read)
        if n < record_size:
            break


print(f'buf read is: {buf_read}')
memory_val = memoryview(buf_read)
memory_val = memory_val[-3:]
print(f'memory value is: {memory_val}')
memory_val[:] = b'WORLD'
print(f'buf read is: {buf_read}')

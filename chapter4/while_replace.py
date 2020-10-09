CHUNKSIZE = 8192

def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        # process_data(data)


def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        pass
        # process_data(data)


import sys
file_read = open('/etc/passwd')
for chunk in iter(lambda: file_read.read(10), ''):
    n = sys.stdout.write(chunk)

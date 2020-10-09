file_name = 'test.txt'
with open(file_name, 'wt') as f:
    f.write('Hello world!\n')

with open(file_name, 'xt') as f:
    f.write('Hello\n')


import os
if not os.path.exists(file_name):
    with open(file_name, 'wt') as f:
        f.write('Hello,I am a test.\n')
else:
    print(f'File {file_name} already exists!')


def bad_filename(file_name):
    return repr(file_name)[1:-1]

try:
    print(file_name)
except UnicodeEncodeError:
    print(bad_filename(file_name))


import os
file_list = os.listdir('.')
print(f'{file_list}')



for name in file_list:
    print(f'file name is: {name}')


for name in file_list:
    try:
        print(f'file name is: {name}')
    except UnicodeEncodeError:
        print(bad_filename(name))


import sys
def bad_filename(file_name):
    temp = file_name.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')


for name in file_list:
    try:
        print(f'file name is: {name}')
    except UnicodeEncodeError:
        print(bad_filename(name))

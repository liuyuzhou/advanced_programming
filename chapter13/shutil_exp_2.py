import os.path

file_name = '/davanced_programming/chapter13/spam.py'
print(f'base name is: {os.path.basename(file_name)}')
print(f'dir name is: {os.path.dirname(file_name)}')
print(f'file split: {os.path.split(file_name)}')
print(os.path.join('/new/dir', os.path.basename(file_name)))
print(os.path.expanduser('~/chapter13/spam.py'))

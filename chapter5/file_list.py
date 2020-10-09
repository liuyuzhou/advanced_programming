import os
file_path = '/etc'
name_list = os.listdir(file_path)
print(f'file list of etc is:\n{name_list}')


import os.path

name_list = [name for name in os.listdir(file_path)
             if os.path.isfile(os.path.join(file_path, name))]

dir_name_list = [name for name in os.listdir(file_path)
                 if os.path.isdir(os.path.join(file_path, name))]


py_file_list = [name for name in os.listdir(file_path)
                if name.endswith('.py')]


import glob
py_file_list = glob.glob(f'{file_path}/*.py')

from fnmatch import fnmatch
py_file_list = [name for name in os.listdir(file_path)
                if fnmatch(name, '*.py')]


import os.path
import glob

py_file_list = glob.glob('*.py')

# Get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in py_file_list]
for name, size, mtime in name_sz_date:
    print(f'name={name}, size={size}, mtime={mtime}')

# Alternative: Get file metadata
file_metadata = [(name, os.stat(name)) for name in py_file_list]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
    print(f'name={name}, size={meta.st_size}, mtime={meta.st_mtime}')

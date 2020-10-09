import os
file_path = '/etc/passwd'
test_path = '/etc/test'
print(f"is {file_path} exists: {os.path.exists(file_path)}")
print(f"is {test_path} exists: {os.path.exists(test_path)}")


print(f'{file_path} is a file: {os.path.isfile(file_path)}')
print(f'{file_path} is a dir: {os.path.isdir(file_path)}')
print(f'{file_path} is a link: {os.path.islink(file_path)}')
print(f'{file_path} real path is: {os.path.realpath(file_path)}')


print(f'{file_path} size is: {os.path.getsize(file_path)}')
print(f'{file_path} mtime is: {os.path.getmtime(file_path)}')


print(os.path.getsize('/Users/lyz/Desktop/private/test.docx'))
import os

csv_path = '/usr/test/Data/test.csv'
print(f'{csv_path} base name is: {os.path.basename(csv_path)}')
print(f'{csv_path} dir name is: {os.path.dirname(csv_path)}')
print(f"new path: {os.path.join('tmp', 'data', os.path.basename(csv_path))}")
csv_path = '~/Data/test.csv'
print(f'path expand user is: {os.path.expanduser(csv_path)}')
print(f'{csv_path} splitext is: {os.path.splitext(csv_path)}')
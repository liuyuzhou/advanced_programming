import sys
print(f'sys path: {sys.path}')


import sys
sys.path.insert(0, '/test/dir')
sys.path.insert(0, '/test/dir')


import sys
from os import path
file_path = path.abspath(path.dirname(__file__))
sys.path.insert(0, path.join(file_path, 'test'))
print(f'sys path: {sys.path}')
import os

def find_file(start, name):
    for rel_path, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, rel_path, name)
            print(f'full path is: {os.path.normpath(os.path.abspath(full_path))}')

if __name__ == '__main__':
    find_file('/advanced_programming/chapter13', 'file_input.py')
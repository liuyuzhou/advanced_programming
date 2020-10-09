import urllib.request
import io

url_res = urllib.request.urlopen('http://www.python.org')
f_test = io.TextIOWrapper(url_res, encoding='utf-8')
text_val = f_test.read()


import sys
print(f'sys stdout encoding is: {sys.stdout.encoding}')
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(f'sys stdout new encoding is: {sys.stdout.encoding}')


file_read = open('sample.txt','w')
print(f'file read: {file_read}')
print(f'file buffer: {file_read.buffer}')
print(f'file buffer raw: {file_read.buffer.raw}')


file_read = io.TextIOWrapper(file_read.buffer, encoding='latin-1')
print(f'file read: {file_read}')

file_read.write('Hello')


file_read = open('sample.txt', 'w')
print(f'file read: {file_read}')

b_val = file_read.detach()
print(f'b obj is: {b_val}')
file_read.write('hello')


file_read = io.TextIOWrapper(b, encoding='latin-1')
print(f'file read: {file_read}')


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii',
                              errors='xmlcharrefreplace')
print('pytho\u00f1o')
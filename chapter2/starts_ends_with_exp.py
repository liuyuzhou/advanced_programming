file_name = 'python.txt'
print(file_name.endswith('.txt'))
print(file_name.startswith('abc'))

url_val = 'http://www.python.org'
print(url_val.startswith('http:'))


import os
file_name_list = os.listdir('.')
print(file_name_list)
print([name for name in file_name_list if name.endswith(('.py', '.h')) ])

print(any(name.endswith('.py') for name in file_name_list))


from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


web_pre_list = ['http:', 'ftp:']
url_val = 'http://www.python.org'
print(url_val.startswith(tuple(web_pre_list)))
print(url_val.startswith(web_pre_list))


file_name = 'test.txt'
print(file_name[-4:] == '.txt')

url_val = 'http://www.python.org'
print(url_val[:5] == 'http:' or url_val[:6] == 'https:' or url_val[:4] == 'ftp:')

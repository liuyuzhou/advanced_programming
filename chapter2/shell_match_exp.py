from fnmatch import fnmatch, fnmatchcase

print(fnmatch('python.txt', '*.txt'))
print(fnmatch('hello.txt', '?ello.txt'))

print(fnmatch('course_15.csv', 'course_[0-9]*'))

names = ['Date_1.csv', 'Date_2.csv', 'config.ini', 'test.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])


print(fnmatch('python.txt', '*.TXT'))

print(fnmatchcase('python.txt', '*.TXT'))


doing_thing = [
    'reading a book',
    'watching tv',
    'running in the park',
    'eating food',
    'writing book',
]


from fnmatch import fnmatchcase
print([doing for doing in doing_thing if fnmatchcase(doing, '* book')])
print([doing for doing in doing_thing if fnmatchcase(doing, '[a-z][a-z]*ing *oo*')])
from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')

    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()


f = TemporaryFile('w+t')
# Use the temporary file
f.close()


with TemporaryFile('w+t', encoding='utf-8', errors='ignore') as f:
    pass


from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)
    pass


with NamedTemporaryFile('w+t', delete=False) as f:
    print('filename is:', f.name)
    pass


from tempfile import TemporaryDirectory

with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)
    # Use the directory


import tempfile
print(tempfile.mkstemp())
print(tempfile.mkdtemp())


print(tempfile.gettempdir())

f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')
print(f.name)
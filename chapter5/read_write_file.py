# Read the entire file as a single string
with open('test.txt', 'rt') as f:
    data = f.read()

# Iterate over the lines of the file
with open('test.txt', 'rt') as f:
    for line in f:
        pass


# Write chunks of text data
with open('test.txt', 'wt') as f:
    f.write('text1')
    f.write('text2')

# Redirected print statement
with open('test.txt', 'wt') as f:
    print('line info', file=f)
    print('line info', file=f)


with open('test.txt', 'rt', encoding='latin-1') as f:
    pass


f = open('test.txt', 'rt')
data = f.read()
f.close()


# Read with disabled newline translation
with open('test.txt', 'rt', newline='') as f:
    pass


f = open('hello.txt', 'rt')
print(f.read())

g = open('hello.txt', 'rt', newline='')
print(g.read())


f = open('sample.txt', 'rt', encoding='ascii')
print(f.read())


f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
print(f.read())

g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
print(g.read())

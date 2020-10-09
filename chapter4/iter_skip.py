with open('/etc/passwd') as f:
    for line in f:
        print(f'{line}', end='')


from itertools import dropwhile
with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(f'{line}', end='')


from itertools import islice
items = ['w', 'o', 'r', 12, 5, 7, 90]
for x in islice(items, 3, None):
    print(x)


with open('/etc/passwd') as f:
    # Skip over initial comments
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break

    # Process remaining lines
    while line:
        # Replace with useful processing
        print(line, end='')
        line = next(f, None)


with open('/etc/passwd') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')
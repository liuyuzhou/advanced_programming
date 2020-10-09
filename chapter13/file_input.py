import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')


import fileinput

with fileinput.input('/etc/passwd') as f:
    for line in f:
        print(f.filename(), f.lineno(), line, end='')
test_list = ['a', 'b', 'c']
for idx, str_val in enumerate(test_list):
    print(f'index is: {idx}, str value is: {str_val}')


for idx, str_val in enumerate(test_list, 1):
    print(f'index is: {idx}, str value is: {str_val}')


def parse_data(file_name):
    with open(file_name, 'rt') as f:
        for lno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print(f'Line {lno}: Parse error: {e}')


from collections import defaultdict

word_summary = defaultdict(list)
with open('/etc/passwd', 'r') as f:
    line_list = f.readlines()

for idx, line in enumerate(line_list):
    # Create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)


lno = 1
f = open('/etc/passwd')
for line in f:
    # Process line
    lno += 1


for lno, line in enumerate(f):
    # Process line
    pass


data_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Correct!
for n, (x, y) in enumerate(data_list):
    pass

# Error!
for n, x, y in enumerate(data_list):
    pass
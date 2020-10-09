test_list = ['Life', 'is', 'short', 'Use', 'python']
print(' '.join(test_list))
print(','.join(test_list))


a_str = 'Life is short'
b_str = 'Use python'
print(a_str + ',' + b_str)


print(f'{a_str},{b_str}')


str_val = ''
for test_str in test_list:
    str_val += test_str
print(str_val)


data_list = ['python', 23, 2020.4]
print(','.join(str(d) for d in data_list))


c_str = 'Let together'
# not support
print(a_str + ':' + b_str + ':' + c_str)
# not support
print(':'.join([a_str, b_str, c_str]))
# support,is better
print(a_str, b_str, c_str, sep=':')


# Version 1 (string concatenation)
f.write(chunk1 + chunk2)

# Version 2 (separate I/O operations)
f.write(chunk1)
f.write(chunk2)


def sample_func():
    yield 'Life'
    yield 'is'
    yield 'short'
    yield 'Use'
    yield 'python'


text_val = ''.join(sample_func())

for str_val in sample_func():
    f.write(str_val)


def combine_obj(source, max_size):
    str_list = []
    size = 0
    for item_val in source:
        str_list.append(item_val)
        size += len(item_val)
        if size > max_size:
            yield ''.join(str_list)
            str_list = []
            size = 0
    yield ''.join(str_list)

with open('file_name', 'w') as f:
    for str_val in combine_obj(sample_func(), 8192):
        f.write(str_val)

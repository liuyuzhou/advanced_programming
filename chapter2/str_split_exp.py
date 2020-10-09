import re

line = 'hello world; life is short,use, python, best'
# 使用正则做分割
print(re.split(r'[;,\s]\s*', line))


sub_line_list = re.split(r'(;|,|\s)\s*', line)
print(sub_line_list)


val_list = sub_line_list[::2]
print(val_list)
delimiters = sub_line_list[1::2] + ['']
print(delimiters)
print(' '.join(v+d for v,d in zip(val_list, delimiters)))



print(re.split(r'(?:,|;|\s)\s*', line))
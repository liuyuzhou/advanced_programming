test_str = ' hello world \n  '
print(f'去除前后空格：{test_str.strip()}')
print(f'去除左侧空格：{test_str.lstrip()}')
print(f'去除右侧空格：{test_str.rstrip()}')

test_t = '===== hello--world-----'
print(test_t.rstrip('-'))
print(test_t.strip('-='))


test_s = ' hello world  \n  '
print(test_s.strip())


print(test_s.replace(' ', ''))
import re
print(re.sub('\s+', '', test_s))


file_name = '/path/path'
with open(file_name) as file:
    lines = (line.strip() for line in file)
    for line in lines:
        print(line)

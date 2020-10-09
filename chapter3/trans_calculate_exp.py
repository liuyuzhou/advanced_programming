num_list = [1, 2, 3, 4, 5]
print(sum(x * x for x in num_list))


import os
file_list = os.listdir('dirname')
if any(name.endswith('.py') for name in file_list):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
course = ('python', 20, 0.3)
print(','.join(str(x) for x in course))

# Data reduction across fields of a data structure
course_info = [
    {'name':'python', 'score': 100.0},
    {'name':'java', 'score': 85.0},
    {'name':'c', 'score': 90.0},
    {'name':'c++', 'score': 95.0}
]
min_score = min(cf['score'] for cf in course_info)
print(min_score)


# 显式的传递一个生成器表达式对象
print(sum((x * x for x in num_list)))
# 更加优雅的实现方式，省略了括号
print(sum(x * x for x in num_list))


num_list = [1, 2, 3, 4, 5]
print(sum([x * x for x in num_list]))


print(min(cf['score'] for cf in course_info))
print(min(course_info, key=lambda cf: cf['score']))
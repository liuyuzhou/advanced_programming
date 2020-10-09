course = 'python'
class_num = 20
score = 0.3
print(course, class_num, score)
print(course, class_num, score, sep=',')
print(course, class_num, score, sep=',', end='!\n')


for i in range(5):
    print(i)

for i in range(5):
    print(i, end=' ')


print(','.join((course,f'{class_num}',f'{score}')))


row = (course, class_num, score)
print(','.join(row))
print(','.join(str(x) for x in row))


print(*row, sep=',')

course_score = {
    '高等代数': 100.0,
    '算法与数据结构': 92.0,
    '编译原理': 88.5,
    '数学分析': 97.5,
    '统计学原理': 90.5
}

min_score = min(zip(course_score.values(), course_score.keys()))
print(f'最低得分课程及得分：{min_score[1]} {min_score[0]}')
max_score = max(zip(course_score.values(), course_score.keys()))
print(f'最高得分课程及得分：{max_score[1]} {max_score[0]}')

score_sorted = sorted(zip(course_score.values(), course_score.keys()))
print(score_sorted)

score_and_course = zip(course_score.values(), course_score.keys())
# ok，print is normal
print(min(score_and_course))
# ValueError: max() arg is an empty sequence
# print(max(score_and_course))

print(min(course_score)) # 数学分析
print(max(course_score)) # 高等代数

print(min(course_score.values())) # 88.5
print(max(course_score.values())) # 100.0

print(min(course_score, key=lambda k: course_score[k])) # 编译原理
print(max(course_score, key=lambda k: course_score[k])) # 高等代数

min_score = course_score[min(course_score, key=lambda k: course_score[k])]
print(min_score)

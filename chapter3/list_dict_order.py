from operator import itemgetter

student_info = [
    {'name': 'xiao meng', 'age': 12, 'number': 1003},
    {'name': 'xiao ming', 'age': 12, 'number': 1002},
    {'name': 'xiao zhi', 'age': 11, 'number': 1001},
    {'name': 'xiao li', 'age': 12, 'number': 1004}
]

order_by_name = sorted(student_info, key=itemgetter('name'))
order_by_number = sorted(student_info, key=itemgetter('number'))
print(order_by_name)
print(order_by_number)

order_by_name_age = sorted(student_info, key=itemgetter('name','age'))
print(order_by_name_age)

order_by_name = sorted(student_info, key=lambda r: r['name'])
order_by_age_number = sorted(student_info, key=lambda r: (r['age'],r['number']))
print(order_by_name)
print(order_by_age_number)

print(min(student_info, key=itemgetter('number')))
print(max(student_info, key=itemgetter('number')))
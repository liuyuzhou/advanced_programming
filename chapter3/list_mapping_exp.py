from collections import namedtuple

UserInfo = namedtuple('UserInfo', ['email', 'date'])
user_info = UserInfo('test@ai.com', '2012-10-19')
print(user_info)
print(user_info.email)
print(user_info.date)


print(len(user_info))
email, date = user_info
print(email, date)


def calculate_cost_1(record_list):
    total = 0.0
    for record in record_list:
        total += record[1] * record[2]
    return total


from collections import namedtuple

Course = namedtuple('Course', ['name', 'class_hour', 'score'])
def calculate_cost(record_list):
    total = 0.0
    for rec in record_list:
        course = Course(*rec)
        total += course.class_hour * course.score
    return total


course = Course('xiao meng', 20, 0.3)
print(course)
course = course._replace(class_hour=30)
print(course)


from collections import namedtuple

Course = namedtuple('Course', ['name', 'class_hour', 'score', 'date', 'time'])

# Create a prototype instance
course_prototype = Course('', 0, 0.0, None, None)

# Function to convert a dictionary to a Course
def dict_to_course(course):
    return course_prototype._replace(**course)


course_a = {'name': 'xiao meng', 'class_hour': 20, 'score': 0.3}
print(dict_to_course(course_a))
course_b = {'name': 'xiao meng', 'class_hour': 20, 'score': 0.3, 'date': '04/19/2020'}
print(dict_to_course(course_b))
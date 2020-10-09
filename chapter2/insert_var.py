language_name = 'Python'
age = 30
test_str = f'{language_name} is {age}.'
print(test_str)


print(test_str.format_map(vars()))


class Info:
    def __init__(self, language_name, age):
        self.language_name = language_name
        self.age = age

info = Info('Python', 30)
print(test_str.format_map(vars(info)))


import string
str_t = string.Template('$language_name is $age.')
print(str_t.substitute(vars()))

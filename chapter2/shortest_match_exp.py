import re
str_pat = re.compile(r'"(.*)"')
text_val = 'Show "no." on screen'
print(str_pat.findall(text_val))

text_v = 'Computer show "no." Phone show "yes."'
print(str_pat.findall(text_v))


str_pat = re.compile(r'"(.*?)"')
print(str_pat.findall(text_v))

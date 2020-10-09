test_str = "PyCons take place throughout many parts of the world. \
Each PyCon is different in its own way;  drawing from its \
own geographical location as well as local history and culture. \
In 2017 another beautiful country opened its doors to a new PyCon, \
with the launch of PyCon Colombia. "


import textwrap
print(textwrap.fill(test_str, 70))

print(textwrap.fill(test_str, 40))

print(textwrap.fill(test_str, 40, initial_indent='    '))

print(textwrap.fill(test_str, 40, subsequent_indent='    '))


import os
print(os.get_terminal_size().columns)

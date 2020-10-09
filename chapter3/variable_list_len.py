record_list = [
    ('f_func', 1, 2),
    ('d_func', 'hello world'),
    ('f_func', 'a', 'b'),
]


def f_func(x, y):
    print(f'f func:{x} {y}')


def d_func(s):
    print(f'd func:{s}')


for tag, *args in record_list:
    if tag == 'f_func':
        f_func(*args)
    elif tag == 'd_func':
        d_func(*args)

def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

print(f'avg = {avg(3, 6)}')
print(f'avg = {avg(1, 3, 7, 9)}')


import html

def make_element(name, value, **attrs):
    key_val_list = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(key_val_list)
    element = f'<{name}{attr_str}>{html.escape(value)}</{name}>'
    return element

print(f"make element: {make_element('item', 'Albatross', size='large', quantity=6)}")

print(f"make element: {make_element('p', '<spam>')}")


def any_args(*args, **kwargs):
    print(args)
    print(kwargs)


def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):
    pass

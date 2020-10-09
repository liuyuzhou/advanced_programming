a = 20
exec('b = a + 1')
print(f'b = {b}')


# def test():
#     a = 20
#     exec('b = a + 1')
#     print(f'b = {b}')
#
# test()


def test():
    a = 20
    loc = locals()
    exec('b = a + 1')
    b = loc['b']
    print(f't: b = {b}')

test()


def test_1():
    x = 0
    exec('x += 1')
    print(f't1: x = {x}')

test_1()


def test_2():
    x = 0
    loc = locals()
    print(f't2 before: {loc}')
    exec('x += 1')
    print(f't2 after: {loc}')
    print(f't2: x = {x}')

test_2()


def test_3():
    x = 0
    loc = locals()
    print(f't3: loc = {loc}')
    exec('x += 1')
    print(f't3: loc = {loc}')
    locals()
    print(f't3: loc = {loc}')

test_3()


def test_4():
    a = 20
    loc = {'a': a}
    glb = {}
    exec('b = a + 1', glb, loc)
    b = loc['b']
    print(f't4: b = {b}')

test_4()
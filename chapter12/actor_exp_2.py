def print_actor():
    while True:

        try:
            msg = yield
            print(f'Got: {msg}')
        except GeneratorExit:
            print('Actor terminating')

p = print_actor()
next(p)
p.send('Hello')
p.send('World')
p.close()
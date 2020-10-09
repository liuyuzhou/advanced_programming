def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


def print_result(result):
    print(f'print result. Got: {result}')

def add(x, y):
    return x + y

apply_async(add, (3, 5), callback=print_result)

apply_async(add, ('Hello ', 'World'), callback=print_result)


class ResultHandler:

    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print(f'result handler. [{self.sequence}] Got: {result}')


r = ResultHandler()
apply_async(add, (3, 5), callback=r.handler)
apply_async(add, ('Hello ', 'World'), callback=r.handler)


def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print(f'make handler. [{sequence}] Got: {result}')
    return handler


handler = make_handler()
apply_async(add, (3, 5), callback=handler)
apply_async(add, ('Hello ', 'World'), callback=handler)


def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print(f'make handler use generator. [{sequence}] Got: {result}')


handler = make_handler()
next(handler)
apply_async(add, (3, 5), callback=handler.send)
apply_async(add, ('Hello ', 'World'), callback=handler.send)

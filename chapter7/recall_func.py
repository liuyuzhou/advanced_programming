def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


from queue import Queue
from functools import wraps

class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args

def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper


def add(x, y):
    return x + y

@inlined_async
def test():
    result = yield Async(add, (3, 5))
    print(f'number add result: {result}')
    result = yield Async(add, ('Hello ', 'World'))
    print(f'str add result: {result}')
    for n in range(10):
        result = yield Async(add, (n, n))
        print(f'async cycle result: {result}')
    print('Goodbye')


if __name__ == '__main__':
    import multiprocessing
    pool = multiprocessing.Pool()
    apply_async = pool.apply_async

    test()

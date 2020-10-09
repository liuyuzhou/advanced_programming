import time
from contextlib import contextmanager

@contextmanager
def time_use(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f'{label}: {end - start} s')

with time_use('counting'):
    n = 10000000
    while n > 0:
        n -= 1


@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working


item_list = [1, 2, 3]
with list_transaction(item_list) as working:
    working.append(4)
    working.append(5)

print(f'items is: {item_list}')
with list_transaction(item_list) as working:
    working.append(6)
    working.append(7)
    raise RuntimeError('oops')

print(f'items is: {item_list}')


import time

class time_use:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_ty, exc_val, exc_tb):
        end = time.time()
        print(f'{self.label}: {end - self.start} s')
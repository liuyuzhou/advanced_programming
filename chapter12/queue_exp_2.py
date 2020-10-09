from queue import Queue
from threading import Thread

_sentinel = object()

def producer(out_q):
    put_time = 0
    while True:
        data = 'hello world!'
        out_q.put(data)

        put_time += 1
        if put_time == 5:
            out_q.put(_sentinel)

def consumer(in_q):
    while True:
        data = in_q.get()
        print(f'get data is: {data}')

        if data is _sentinel:
            in_q.put(_sentinel)
            break

q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
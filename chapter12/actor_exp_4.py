from threading import Event
from chapter12.actor_exp_1 import Actor

class Result:
    def __init__(self):
        self._evt = Event()
        self._result = None

    def set_result(self, value):
        self._result = value

        self._evt.set()

    def result(self):
        self._evt.wait()
        return self._result

class Worker(Actor):
    def submit(self, func, *args, **kwargs):
        r = Result()
        self.send((func, args, kwargs, r))
        return r

    def run(self):
        while True:
            func, args, kwargs, r=self.recv()
            r.set_result(func(*args, **kwargs))

worker = Worker()
worker.start()
r = worker.submit(pow, 2, 3)
worker.close()
worker.join()
print(r.result())

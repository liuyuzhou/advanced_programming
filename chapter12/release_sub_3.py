from chapter12.release_sub_1 import get_exchange

class DisplayMessages:
    def __init__(self):
        self.count = 0
    def send(self, msg):
        self.count += 1
        print(f'msg[{self.count}]: {msg!r}')

exc = get_exchange('name')
d = DisplayMessages()
exc.attach(d)


exc = get_exchange('name')
exc.attach(some_task)
try:
    ...
finally:
    exc.detach(some_task)
import select
import threading
from chapter12.queue_loop_1 import PollableQueue

def consumer(queues):
    while True:
        can_read, _, _ = select.select(queues,[],[])
        for r in can_read:
            item = r.get()
            print(f'Got: {item}')

q1 = PollableQueue()
q2 = PollableQueue()
q3 = PollableQueue()
t = threading.Thread(target=consumer, args=([q1,q2,q3],))
t.daemon = True
t.start()

q1.put(3)
q2.put(21)
q3.put('hello world!')
q2.put(18)
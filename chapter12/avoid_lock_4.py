import threading
from chapter12.avoid_lock_1 import acquire

# The philosopher thread
def philosopher(left, right):
    while True:
        with acquire(left,right):
             print(f'{threading.currentThread()} eating')

# The chopsticks (represented by locks)
NSTICKS = 5
chopsticks = [threading.Lock() for n in range(NSTICKS)]

# Create all of the philosophers
for n in range(NSTICKS):
    t = threading.Thread(target=philosopher,
                         args=(chopsticks[n],chopsticks[(n+1) % NSTICKS]))
    t.start()
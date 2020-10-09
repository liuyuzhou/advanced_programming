from chapter13.timer_exp import Timer

def countdown(n):
    while n > 0:
        n -= 1

t = Timer()
t.start()
countdown(1000000)
t.stop()
print(f'time used: {t.elapsed}')

with t:
    countdown(1000000)

print(f'use with time use: {t.elapsed}')

with Timer() as t2:
    countdown(1000000)
print(f't2 time used: {t2.elapsed}')


import time
t = Timer(time.process_time)
with t:
    countdown(1000000)
print(f'process time use: {t.elapsed}')
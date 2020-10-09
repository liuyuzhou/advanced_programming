import time

def consumer(queues):
    while True:
        for q in queues:
            if not q.empty():
                item = q.get()
                print(f'Got: {item}')

        time.sleep(0.01)
from queue import Queue
from threading import Thread, Event

# A thread that produces data
def producer(out_q):
    while True:
        # Produce some data
        ...
        # Make an (data, event) pair and hand it to the consumer
        evt = Event()
        data = ''
        out_q.put((data, evt))
        ...
        # Wait for the consumer to process the item
        evt.wait()

def consumer(in_q):
    while True:
        data, evt = in_q.get()
        # Process the data
        ...
        # Indicate completion
        evt.set()
import select

def event_loop(sockets, queues):
    while True:
        # polling with a timeout
        can_read, _, _ = select.select(sockets, [], [], 0.01)
        for r in can_read:
            # handle_read(r)
            pass
        for q in queues:
            if not q.empty():
                item = q.get()
                print(f'Got: {item}')
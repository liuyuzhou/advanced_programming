def test_func(a, b, c, d):
    return a, b, c, d


from functools import partial
tf_val_1 = partial(test_func, 1)
print(f'partial 1: {tf_val_1(2, 3, 4)}')
print(f'partial 1: {tf_val_1(4, 5, 6)}')
tf_val_2 = partial(test_func, d=42)
print(f'partial 42: {tf_val_2(1, 2, 3)}')
print(f'partial 42: {tf_val_2(4, 5, 5)}')
tf_val_3 = partial(test_func, 1, 2, d=42)
print(f'not partial 3: {tf_val_3(3)}')
print(f'not partial 4: {tf_val_3(4)}')
print(f'not partial 5: {tf_val_3(5)}')


point_list = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

import math
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


pt = (4, 3)
point_list.sort(key=partial(distance, pt))
print(f'point list: {point_list}')


def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)

# A sample function
def add(x, y):
    return x + y

if __name__ == '__main__':
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()


from socketserver import StreamRequestHandler, TCPServer

class EchoHandler(StreamRequestHandler):
    def handle(self):
        for line in self.rfile:
            self.wfile.write(b'GOT:' + line)

serv = TCPServer(('', 56271), EchoHandler)
serv.serve_forever()


class EchoHandler(StreamRequestHandler):
    # ack is added keyword-only argument. *args, **kwargs are
    # any normal parameters supplied (which are passed on)
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)


from functools import partial
serv = TCPServer(('', 12222), partial(EchoHandler, ack=b'RECEIVED:'))
serv.serve_forever()


point_list.sort(key=lambda p: distance(pt, p))
p.apply_async(add, (3, 4), callback=lambda result: output_result(result,log))
serv = TCPServer(('', 13333),
        lambda *args, **kwargs: EchoHandler(*args, ack=b'RECEIVED:', **kwargs))
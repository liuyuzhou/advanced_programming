# from xmlrpc.server import SimpleXMLRPCServer
# def add(x,y):
#     return x+y
#
# serv = SimpleXMLRPCServer(('', 15000))
# serv.register_function(add)
# serv.serve_forever()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

from xmlrpc.client import ServerProxy

s = ServerProxy('http://localhost:15000', allow_none=True)
p = Point(2, 3)
s.set('foo', p)
print(f"get foo is: {s.get('foo')}")


s.set('foo', b'Hello World')
print(f"get foo is: {s.get('foo')}")

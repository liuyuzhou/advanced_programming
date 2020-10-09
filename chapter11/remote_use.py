from multiprocessing.connection import Client
from chapter11.rpc_proxy import RPCProxy

c = Client(('localhost', 17000), authkey=b'peekaboo')
proxy = RPCProxy(c)
print(f'add(3, 5) = {proxy.add(3, 5)}')
print(f'sub(5, 12) = {proxy.sub(5, 12)}')
proxy.sub([1, 2], 4)
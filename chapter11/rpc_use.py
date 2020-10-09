from xmlrpc.client import ServerProxy

s = ServerProxy('http://localhost:15000', allow_none=True)
s.set('foo', 'bar')
s.set('spam', [1, 2, 3])
print(f'keys: {s.keys()}')
print(f"get foo is: {s.get('foo')}")
print(f"get spam is: {s.get('spam')}")
s.delete('spam')
print(f"exists spam is: {s.exists('spam')}")

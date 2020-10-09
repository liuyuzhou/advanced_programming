from xmlrpc.client import ServerProxy
s = ServerProxy('https://localhost:15000', allow_none=True)
s.set('foo','bar')
s.set('spam', [1, 2, 3])
s.keys()
s.get('foo')
s.get('spam')
s.delete('spam')
s.exists('spam')

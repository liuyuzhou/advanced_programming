from unittest.mock import patch

x = 30
with patch('__main__.x'):
    print(f'x object is: {x}')

print(f'x is: {x}')


with patch('__main__.x', 'patched_value'):
    print(f'x new value: {x}')


from unittest.mock import MagicMock
m = MagicMock(return_value = 10)
print(f'value: {m(1, 2, debug=True)}')
m.assert_called_with(1, 2, debug=True)
m.assert_called_with(1, 2)

m.upper.return_value = 'HELLO'
print(f"upper result: {m.upper('hello')}")
assert m.upper.called

m.split.return_value = ['hello', 'world']
print(f"split result: {m.split('hello world')}")
m.split.assert_called_with('hello world')

print(f"object is: {m['blah']}")
print(f'called result: {m.__getitem__.called}')
m.__getitem__.assert_called_with('blah')
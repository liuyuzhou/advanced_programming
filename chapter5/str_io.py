import io

s_obj = io.StringIO()
s_obj.write('Hello World\n')
print('This is a test', file=s_obj)
print(f's obj get value: {s_obj.getvalue()}')
s_obj = io.StringIO('Hello\nWorld\n')
print(f'read point size: {s_obj.read(4)}')
print(f'read: {s_obj.read()}')


s_obj = io.BytesIO()
s_obj.write(b'binary data')
print(f'get value: {s_obj.getvalue()}')
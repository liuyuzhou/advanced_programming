s_obj = b'hello'
import base64

code_obj = base64.b64encode(s_obj)
print(f'b64 encode {s_obj} = {code_obj}')

print(f'decode {code_obj} = {base64.b64decode(code_obj)}')


code_obj = base64.b64encode(s_obj).decode('ascii')
print(f'encode decode {s_obj}= {code_obj}')

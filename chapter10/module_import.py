import importlib

math = importlib.import_module('math')
print(f'math.sqrt(10) = {math.sqrt(10)}')

req = importlib.import_module('requests')
res = req.get('http://www.python.org')
print(f'response text:\n{res.text}')


module_split = importlib.import_module('module_split', __package__)
module_split.course()
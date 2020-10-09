import imp
import requests
import sys

def load_module(url):
    u = requests.get(url)
    source = u.text
    mod = sys.modules.setdefault(url, imp.new_module(source))
    code = compile(source, url, 'exec')
    mod.__file__ = url
    mod.__package__ = ''
    exec(code, mod.__dict__)
    return mod


fib = load_module('http://localhost:15000/fib.py')
print(f'fib(20) = {fib.fib(20)}')

spam = load_module('http://localhost:15000/spam.py')
spam.hello('world')

print(f'{fib}')
print(f'{spam}')
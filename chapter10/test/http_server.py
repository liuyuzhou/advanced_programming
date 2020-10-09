import requests
res = requests.get('http://localhost:15000/fib.py')
data = res.text
print(data)
import requests

req = requests.get('http://localhost:8080/hello?name=world')
print(f'hello text:\n{req.text}')

req = requests.get('http://localhost:8080/localtime')
print(f'localtime text:\n{req.text}')

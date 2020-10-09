import requests

r = requests.get('http://httpbin.org/get?name=Dave&n=37',
                 headers = { 'User-agent': 'goaway/1.0' })

resp = r.json()
print(f"headers:\n{resp['headers']}")
print(f"args: {resp['args']}")
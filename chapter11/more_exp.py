import requests

resp = requests.get('http://www.python.org')

status = resp.status_code
x_timer = resp.headers['X-Timer']
content_type = resp.headers['Content-Type']
content_length = resp.headers['Content-Length']


import requests

resp = requests.get('http://pypi.python.org/pypi?:action=login',
                    auth=('user','password'))


import requests

url = 'http://pypi.python.org'
# First request
resp1 = requests.get(url)

# Second requests with cookies received on first requests
resp2 = requests.get(url, cookies=resp1.cookies)


import requests
url = 'http://httpbin.org/post'
file_list = {'file': ('data.csv', open('data.csv', 'rb'))}

r = requests.post(url, files=file_list)
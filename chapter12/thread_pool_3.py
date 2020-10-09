from concurrent.futures import ThreadPoolExecutor
import requests

def fetch_url(url):
    u = requests.get(url)
    data = u.text
    return data

pool = ThreadPoolExecutor(10)
a = pool.submit(fetch_url, 'http://www.python.org')
b = pool.submit(fetch_url, 'http://www.pypy.org')

x = a.result()
y = b.result()
print(x)
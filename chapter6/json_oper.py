import json

data = {
    'course' : 'python',
    'total_class' : 30,
    'score' : 0.3
}

json_str = json.dumps(data)


data = json.loads(json_str)


# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)


print(json.dumps(False))
str_dict = {'a': True,
            'b': 'Hello',
            'c': None
            }
print(f'dumps result: {json.dumps(str_dict)}')


import requests
import json
response = requests.get('https://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid='
            '0x9b8c139c000d912c&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie='
            'utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3='
            '9&rsv_sug1=10&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT='
            '3635&rsv_sug4=4246&rsv_sug=2')
resp = response.text
from pprint import pprint
pprint(resp)


s = '{"course": "python", "total_class": 30, "score": 0.3}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print(f'data loads: {data}')


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

data = json.loads(s, object_hook=JSONObject)
print(f'course is: {data.course}')
print(f'total class is: {data.total_class}')
print(f'score is: {data.score}')


# print(f'data dumps: {json.dumps(data)}')
# print(f'dumps indent {json.dumps(data, indent=4)}')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 3)
# print(f'dumps: {json.dumps(p)}')


def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d


# Dictionary mapping names to known classes
classes = {
    'Point' : Point
}

def unserialize_object(d):
    # clsname = d.pop('__classname__', None)
    if (clsname := d.pop('__classname__', None)):
        cls = classes[clsname]
        obj = cls.__new__(cls) # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d


p = Point(2,3)
s = json.dumps(p, default=serialize_instance)
a = json.loads(s, object_hook=unserialize_object)
print(f'json loads: {a}')
print(f'a x is: {a.x}')
print(f'a y is: {a.y}')

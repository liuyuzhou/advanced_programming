from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 'abc'
ordered_dict['c'] = 'hello world'
ordered_dict['d'] = -5
for key in ordered_dict:
    print(f'get key is:{key}, value is:{ordered_dict[key]}')

import json
print(json.dumps(ordered_dict))

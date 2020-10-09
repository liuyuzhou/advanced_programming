a_dict = {'x': 1, 'z': 3 }
b_dict = {'y': 2, 'z': 4 }


from collections import ChainMap
c_dict = ChainMap(a_dict, b_dict)
# Outputs 1 (from a_dict)
print(c_dict['x'])
# Outputs 2 (from b_dict)
print(c_dict['y'])
# Outputs 3 (from a_dict)
print(c_dict['z'])


print(len(c_dict))
print(list(c_dict.keys()))
print(list(c_dict.values()))


c_dict['z'] = 10
c_dict['w'] = 40
del c_dict['x']
print(a_dict)
# del c_dict['y']


val_dict = ChainMap()
val_dict['x'] = 1

val_dict = val_dict.new_child()
val_dict['x'] = 2

val_dict = val_dict.new_child()
val_dict['x'] = 3
print(val_dict)
print(val_dict['x'])

val_dict = val_dict.parents
print(val_dict['x'])

val_dict = val_dict.parents
print(val_dict['x'])

print(val_dict)


a_dict = {'x': 1, 'z': 3 }
b_dict = {'y': 2, 'z': 4 }

dict_merge = dict(b_dict)
dict_merge.update(a_dict)
print(dict_merge['x'])
print(dict_merge['y'])
print(dict_merge['z'])


a_dict['x'] = 10
print(dict_merge['x'])


chain_dict = ChainMap(a_dict, b_dict)
print(chain_dict['x'])

a_dict['x'] = 20
print(chain_dict['x'])
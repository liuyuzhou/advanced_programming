a_dict = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b_dict = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# Find keys in common
print(a_dict.keys() & b_dict.keys())
# Find keys in a that are not in b
print(a_dict.keys() - b_dict.keys())
# Find (key,value) pairs in common
print(a_dict.items() & b_dict.items())

# Make a new dictionary with certain keys removed
c = {key:a_dict[key] for key in a_dict.keys() - {'z', 'w'}}
print(c) # c is {'x': 1, 'y': 2}
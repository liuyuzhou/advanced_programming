uni_str_1 = 'Spicy Jalape\u00f1o'
uni_str_2 = 'Spicy Jalapen\u0303o'
print(uni_str_1)
print(uni_str_2)
print(uni_str_1 == uni_str_2)
print(len(uni_str_1))
print(len(uni_str_2))


import unicodedata

t_1 = unicodedata.normalize('NFC', uni_str_1)
t_2 = unicodedata.normalize('NFC', uni_str_2)
print(t_1 == t_2)
print(ascii(t_1))
t_3 = unicodedata.normalize('NFD', uni_str_1)
t_4 = unicodedata.normalize('NFD', uni_str_2)
print(t_3 == t_4)
print(ascii(t_3))


test_str = '\ufb01'
print(test_str)
print(unicodedata.normalize('NFD', test_str))
print(unicodedata.normalize('NFKD', test_str))
print(unicodedata.normalize('NFKC', test_str))


test_1 = unicodedata.normalize('NFD', uni_str_1)
print(''.join(c for c in test_1 if not unicodedata.combining(c)))

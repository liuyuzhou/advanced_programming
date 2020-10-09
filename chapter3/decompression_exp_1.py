# tuple decompression
num_tup = (1, 2)
x, y = num_tup
print(f'x is:{x}, y is:{y}')

# 变量个数和序列元素的个数要匹配，否则产生异常
num_tup = (1, 2)
try:
    x, y, z = num_tup
except Exception as ex:
    print(f'出错了，出错原因:{ex}')

# list object decompression
obj_list = ['abc', 10, 22.2, (2020, 3, 15)]
str_obj, int_obj, float_obj, tuple_obj = obj_list
print(f'tuple_obj is:{tuple_obj}')

# int,float,tuple object decompression
str_obj, int_obj, float_obj, (year, month, day) = obj_list
print(f'year is:{year}, month is:{month}, day is:{day}')

# str object decompression
str_var = 'hello'
a, b, c, d, e = str_var
print(f'the value of a is:{a}')

_, _, f_obj, _ = obj_list
print(f'f_obj is:{f_obj}')

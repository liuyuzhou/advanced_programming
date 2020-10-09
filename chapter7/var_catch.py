x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y


print(f'a(20) = {a(20)}')
print(f'b(20) = {b(20)}')


x = 15
print(f'when x=15,a(15) = {a(15)}')
x = 3
print(f'when x=3,a(15) = {a(15)}')


x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(f'a(15) = {a(15)}')
print(f'b(15) = {b(15)}')


func_list = [lambda x: x+n for n in range(5)]
for i, val in enumerate(func_list):
    print(f'f({i}) = {val(0)}')


func_list = [lambda x, n=n: x+n for n in range(5)]
for i,val in enumerate(func_list):
    print(f'f({i}) = {val(0)}')
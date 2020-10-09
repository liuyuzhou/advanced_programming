a = 2.1
b = 4.2
print(a + b)


from decimal import Decimal
a = Decimal('2.1')
b = Decimal('4.2')
print(f'a + b = {a + b}')


from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(f'a / b = {a / b}')
with localcontext() as ctx:
    ctx.prec = 3
    print(f'a / b = {a / b}')

with localcontext() as ctx:
    ctx.prec = 50
    print(f'a / b = { a / b}')


num_list = [1.23e+18, 1, -1.23e+18]
print(f'sum result is: {sum(num_list)}')


import math
print(f'math sum result: {math.fsum(num_list)}')
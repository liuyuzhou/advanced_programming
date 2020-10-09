a = float('inf')
b = float('-inf')
c = float('nan')
print(f"float('inf') = {a}")
print(f"float('-inf') = {b}")
print(f"float('nan') = {c}")


import math
print(f"float('inf') type is inf: {math.isinf(a)}")
print(f"float('nan') type is nan: {math.isnan(c)}")


print(f'{a} + 45 = {a + 45}')
print(f'{a} * 45 = {a * 45}')
print(f'45 / {a} = {45 / a}')


print(f'{a} / {a} = {a / a}')
print(f'{a} + {b} = {a + b}')


print(f'{c} + 10 = {c + 10}')
print(f'{c} * 10 = {c * 10}')
print(f'{c} / 10 = {c / 10}')
print(f'math.sqrt({c}) = {math.sqrt(c)}')


d = float('nan')
print(f'{c} == {d} is:{c == d}')
print(f'{c} is {d} is:{c is d}')

a = complex(2, 4)
b = 3 - 5j
print(f'complex(2, 4) is: {a}')
print(f'{b}')


print(f'real of {a} is: {a.real}')
print(f'imag of {a} is: {a.imag}')
print(f'conjugate of {a} is: {a.conjugate()}')


print(f'{a} + {b} = {a + b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'abs({a}) = {abs(a)}')


import cmath
print(f'cmath.sin({a}) = {cmath.sin(a)}')
print(f'cmath.cos({a}) = {cmath.cos(a)}')
print(f'cmath.exp({a}) = {cmath.exp(a)}')


import numpy as np
np_a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(f'np_a object is: {np_a}')
print(f'{np_a} + 2 = {np_a + 2}')
print(f'np.sin({np_a}) = {np.sin(np_a)}')


import math
print(math.sqrt(-1))


print(f'cmath.sqrt(-1) = {cmath.sqrt(-1)}')
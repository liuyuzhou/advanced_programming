x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

print(f'{x} * 2 is: {x * 2}')
# print(x + 10)

print(f'{x} + {y} = {x + y}')

import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])

print(f'{ax} * 2 = {ax * 2}')
print(f'{ax} + 10 = {ax + 10}')
print(f'{ax} + {ay} = {ax + ay}')
print(f'{ax} * {ay} = {ax * ay}')


def f(px):
    return 3 * px ** 2 - 2 * px + 7

print(f'f(ax) = {f(ax)}')


print(f'np.sqrt({ax}) = {np.sqrt(ax)}')
print(f'np.cos({ax}) = {np.cos(ax)}')


grid = np.zeros(shape=(10000,10000), dtype=float)
print(f'np.zeros(shape=(10000,10000), dtype=float) result: \n{grid}')


grid += 10
print(f'grid + 10 result:\n{grid}')
print(f'np.sin(grid) result:\n{np.sin(grid)}')


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f'a is:\n{a}')
print(f'a[1] is:\n{a[1]}')
print(f'a[:,1] is:\n{a[:,1]}')
print(f'a[1:3, 1:3] is:\n{a[1:3, 1:3]}')

a[1:3, 1:3] += 10
print(f'a is:\n{a}')
print(f'a + [100, 101, 102, 103] is:\n{a + [100, 101, 102, 103]}')
print(f'np.where(a < 10, a, 10) is:\n{np.where(a < 10, a, 10)}')

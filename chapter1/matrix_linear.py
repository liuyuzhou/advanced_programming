import numpy as np
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print(f'm is:\n{m}')

print(f'm.T is:\n{m.T}')
print(f'm.I is:\n{m.I}')

v = np.matrix([[2],[3],[4]])
print(f'v is:\n{v}')
print(f'm * v is:\n{m * v}')


import numpy.linalg
print(f'numpy.linalg.det(m) is:\n{numpy.linalg.det(m)}')
print(f'numpy.linalg.eigvals(m) is:\n{numpy.linalg.eigvals(m)}')
x = numpy.linalg.solve(m, v)
print(f'x is:\n{x}')
print(f'm * x is:\n{m * x}')
print(f'v is:\n{v}')

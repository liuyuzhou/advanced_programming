x = 1234.56789
print(f'0.2f format {x}: {x:0.2f}')
print(f'>10.1f format {x}: {x: >10.1f}')
print(f'<10.1f format {x}: {x: <10.1f}')
print(f'^10.1f format {x}: {x: ^10.1f}')
print(f', format {x}: {x: ,}')
print(f'0,.1f format {x}: {x: 0,.1f}')


print(f'e format {x} is: {x: e}')
print(f'0.2E format {x} is: {x: 0.2E}')


print(f'The value is {x: 0,.2f}')


print(f'x format: {x: 0.1f}')
print(f'-x format: {-x: 0.1f}')


swap_separators = { ord('.'):',', ord(','):'.' }
print(format(x, ',').translate(swap_separators))

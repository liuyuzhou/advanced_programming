text_str = 'Hello World'
print(text_str.ljust(20))
print(text_str.rjust(20))
print(text_str.center(20))


print(text_str.rjust(20,'='))
print(text_str.center(20, '*'))


print(f'{text_str:>20}')
print(f'{text_str:<20}')
print(f'{text_str:^20}')


print(f'{text_str:=>20}')
print(f'{text_str:*^20}')


print(f'{"hello":>10s} {"world":>10s}')


num = 1.2345
print(f'{num:>10}')
print(f'{num:^5.2f}')



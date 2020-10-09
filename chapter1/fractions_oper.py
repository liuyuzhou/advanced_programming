from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)

print(f'{a} + {b} = {a + b}')
print(f'{a} * {b} = {a * b}')

c = a * b
print(f'numerator of {c} is: {c.numerator}')
print(f'denominator of {c} is: {c.denominator}')

print(f'float({c}) = {float(c)}')

print(f'{c} limit denominator 8 = {c.limit_denominator(8)}')

x = 3.75
print(f'{x} to fractions is: {Fraction(*x.as_integer_ratio())}')
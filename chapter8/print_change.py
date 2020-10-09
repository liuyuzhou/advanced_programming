class FormatChange:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'use repr method: ({self.x!r}, {self.y!r})'

    def __str__(self):
        return f'use str method: ({self.x!s}, {self.y!s})'


fc = FormatChange(5, 7)
print(fc.__repr__())
print(fc)


print(f'fc is {fc!r}')
print(f'fc is {fc}')
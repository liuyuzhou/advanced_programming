a = [1, 2, 3, 4]
print(f'primary a is: {a}')
b = list()
for x in reversed(a):
    b.append(x)
print(f'{a} reversed is: {b}')


f = open('/etc/passwd')
for line in reversed(list(f)):
    print(line, end='')


class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rev_val in reversed(Countdown(20)):
    print(f'reversed order: {rev_val}')
print()
for nor_val in Countdown(20):
    print(f'normal order: {nor_val}')
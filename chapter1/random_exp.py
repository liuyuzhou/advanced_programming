import random
values = [1, 2, 3, 4, 5, 6]
print(f'random choice from {values} is {random.choice(values)}')
print(f'random choice from {values} is {random.choice(values)}')
print(f'random choice from {values} is {random.choice(values)}')


print(f'random sample 2 from {values} is {random.sample(values, 2)}')
print(f'random sample 2 from {values} is {random.sample(values, 2)}')
print(f'random sample 3 from {values} is {random.sample(values, 3)}')
print(f'random sample 3 from {values} is {random.sample(values, 3)}')


random.shuffle(values)
print(f'random shuffle is:{values}')
random.shuffle(values)
print(f'random shuffle is:{values}')


print(f'random.randint(0,10) = {random.randint(0,10)}')
print(f'random.randint(0,10) = {random.randint(0,10)}')
print(f'random.randint(0,10) = {random.randint(0,10)}')


print(f'random.random() = {random.random()}')
print(f'random.random() = {random.random()}')
print(f'random.random() = {random.random()}')


print(f'random.getrandbits(200) = {random.getrandbits(200)}')


print(f'random.seed() = {random.seed()}')
print(f'random.seed(123) = {random.seed(123)}')
print(f"random.seed(b'bytedata') = {random.seed(b'bytedata')}")

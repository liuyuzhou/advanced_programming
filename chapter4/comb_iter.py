item_list = ['a', 'b', 'c']
from itertools import permutations
for p in permutations(item_list):
    print(f'all permutations is: {p}')


for p in permutations(item_list, 2):
    print(f'permutations 2 is: {p}')


from itertools import combinations
for c in combinations(item_list, 3):
    print(f'combinations 3 is: {c}')

for c in combinations(item_list, 2):
    print(f'combinations 2 is: {c}')

for c in combinations(item_list, 1):
    print(f'combinations 1 is: {c}')


from itertools import combinations_with_replacement
for c in combinations_with_replacement(item_list, 3):
    print(f'combinations with replacement is: {c}')
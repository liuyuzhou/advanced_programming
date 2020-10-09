import heapq
a_list = [1, 3, 5, 9]
b_list = [2, 4, 6, 10]
for c in heapq.merge(a_list, b_list):
    print(f'order result: {c}')


with open('sorted_file_1', 'rt') as file_1, \
    open('sorted_file_2', 'rt') as file_2, \
    open('merged_file', 'wt') as out_file:
    for line in heapq.merge(file_1, file_2):
        out_file.write(line)
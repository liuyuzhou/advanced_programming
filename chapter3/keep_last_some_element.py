from collections import deque


def search(lines, search_val, history=1):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if search_val in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open(r'test_file/element.txt') as f:
        for search_v, prev_lines in search(f, 'python', 2):
            for pre_line in prev_lines:
                print(pre_line, end='')
            print(f'search value is:{search_v}')

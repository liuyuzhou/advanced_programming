from collections import deque

class LineHistory:
    def __init__(self, line_list, histlen=3):
        self.line_list = line_list
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lno, line in enumerate(self.line_list, 1):
            self.history.append((lno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('/etc/passwd') as f:
    line_list = LineHistory(f)
    for line in line_list:
        if 'WebServer' in line:
            for lno, h_line in line_list.history:
                print(f'{lno}:{h_line}', end='')


file_list = open('/etc/passwd')
line_list = LineHistory(file_list)
# print(next(line_list))

iter_obj = iter(line_list)
print(f'iter obj next is: {next(iter_obj)}')
print(f'iter obj next is: {next(iter_obj)}')
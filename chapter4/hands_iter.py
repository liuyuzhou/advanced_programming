def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                # end 指定为 空，输出行不会有一个空白行
                print(line, end='')
        except StopIteration:
            pass


with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if not line:
            break
        # end 指定为 空，输出行不会有一个空白行
        print(line, end='')


num_list = [1, 2, 3]
items = iter(num_list)
for i in range(len(num_list)):
    print(f'first items next is:{next(items)}')

for i in range(len(num_list) + 1):
    print(f'second items next is:{next(items)}')

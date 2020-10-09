def recv(maxsize, *, block):
    return ''

# recv(1024, True) # TypeError
recv(1024, block=True) # Ok


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(f'min value = {minimum(2, 9, 3, -6, 18)}')
print(f'min value of clip = {minimum(2, 9, 3, -6, 18, clip=0)}')


# msg = recv(1024, False)


msg = recv(1024, block=False)


print(f'help info:\n {help(recv)}')
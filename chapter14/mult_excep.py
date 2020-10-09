try:
    client_obj.get_url(url)
except (URLError, ValueError, SocketTimeout):
    client_obj.remove_url(url)


try:
    client_obj.get_url(url)
except (URLError, ValueError):
    client_obj.remove_url(url)
except SocketTimeout:
    client_obj.handle_url_timeout(url)


try:
    f = open(filename)
except (FileNotFoundError, PermissionError):
    pass


try:
    f = open(filename)
except OSError:
    pass


try:
    f = open(filename)
except OSError as e:
    if e.errno == errno.ENOENT:
        logger.error('File not found')
    elif e.errno == errno.EACCES:
        logger.error('Permission denied')
    else:
        logger.error('Unexpected error: %d', e.errno)


f = open('missing')
try:
    f = open('missing')
except OSError:
    print('It failed')
except FileNotFoundError:
    print('File not found')


print(f'mro is: {FileNotFoundError.__mro__}')
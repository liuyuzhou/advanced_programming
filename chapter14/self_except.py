class NetworkError(Exception):
    pass

class HostnameError(NetworkError):
    pass

class TimeoutError(NetworkError):
    pass

class ProtocolError(NetworkError):
    pass


try:
    msg = s.recv()
except TimeoutError as e:
    ...
except ProtocolError as e:
    ...


try:
    s.send(msg)
except ProtocolError:
    ...


try:
    s.send(msg)
except NetworkError:
    ...


class CustomError(Exception):
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status


try:
    raise RuntimeError('It failed')
except RuntimeError as e:
    print(e.args)

try:
    raise RuntimeError('It failed', 42, 'spam')
except RuntimeError as e:
    print(e.args)
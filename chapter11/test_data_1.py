from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 25000))
s.listen(1)
c,a = s.accept()
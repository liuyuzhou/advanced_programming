from socket import *
c = socket(AF_INET, SOCK_STREAM)
c.connect(('localhost', 25000))
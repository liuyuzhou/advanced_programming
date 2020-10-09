from socket import *
s = socket(AF_INET, SOCK_DGRAM)
print(f"sendto: {s.sendto(b'',('localhost',14000))}")
print(f'recv content: {s.recvfrom(128)}')
print(f"sendto: {s.sendto(b'Hello',('localhost',15000))}")
print(f'recv content: {s.recvfrom(128)}')

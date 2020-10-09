import ipaddress

net = ipaddress.ip_network('193.145.37.64/30')
print(f'net is: {net}')

for n in net:
    print(f'ip address is: {n}')

net_6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/127')
print(f'ip net 6 is: {net_6}')
for n in net_6:
    print(f'net 6 address: {n}')


print(f'num addresses: {net.num_addresses}')
print(f'num 0: {net[0]}')
print(f'num 1: {net[1]}')


a = ipaddress.ip_address('193.145.37.67')
print(f'{a} in net is: {a in net}')
b = ipaddress.ip_address('193.145.37.97')
print(f'{b} in net is: {b in net}')


i_net = ipaddress.ip_interface('193.145.37.67/27')
print(f'network: {i_net.network}')
print(f'ip is: {i_net.ip}')


local_host = ipaddress.ip_address('127.0.0.1')
from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect((a, 8080))
s.connect((str(a), 8080))
import os
file_data = os.open('test.txt', os.O_WRONLY | os.O_CREAT)

# Turn into a proper file
test_file = open(file_data, 'wt')
test_file.write('hello world\n')
test_file.close()


test_file = open(file_data, 'wt', closefd=False)


from socket import socket, AF_INET, SOCK_STREAM

def echo_client(client_sock, addr):
    print(f'Got connection from {addr}')

    # Make text-mode file wrappers for socket reading/writing
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
                closefd=False)

    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1',
                closefd=False)

    # Echo lines back to the client using file I/O
    for line in client_in:
        client_out.write(line)
        client_out.flush()

    client_sock.close()

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)


import sys
bstd_out = open(sys.stdout.fileno(), 'wb', closefd=False)
bstd_out.write(b'Hello World\n')
bstd_out.flush()
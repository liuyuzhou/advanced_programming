from socket import socket, AF_INET, SOCK_STREAM
import ssl

# Private key of the server
KEYFILE = 'server_key.pem'
# Server certificate (given to client)
CERTFILE = 'server_cert.pem'

def echo_client(s):
    while True:
        data = s.recv(8192)
        if data == b'':
            break
        s.send(data)
    s.close()
    print('Connection closed')

def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(1)

    # Wrap with an SSL layer requiring client certs
    s_ssl = ssl.wrap_socket(s, keyfile=KEYFILE, certfile=CERTFILE, server_side=True)
    # Wait for connections
    while True:
        try:
            c,a = s_ssl.accept()
            print(f'Got connection {c} {a}')
            echo_client(c)
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')

echo_server(('', 20000))
import socket
from socketserver import StreamRequestHandler

class EchoHandler(StreamRequestHandler):
    # Optional settings (defaults shown)
    # Timeout on all socket operations
    timeout = 5
    # Read buffer size
    rbufsize = -1
    # Write buffer size
    wbufsize = 0
    # Sets TCP_NODELAY socket option
    disable_nagle_algorithm = False

    def handle(self):
        print(f'Got connection from {self.client_address}')
        try:
            for line in self.rfile:
                # self.wfile is a file-like object for writing
                self.wfile.write(line)
        except socket.timeout:
            print('Timed out!')
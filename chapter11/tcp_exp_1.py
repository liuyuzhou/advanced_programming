from socketserver import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print(f'Got connection from {self.client_address}')
        while True:
            # msg = self.request.recv(8192)
            if not (msg := self.request.recv(8192)):
                break
            self.request.send(msg)
            print(f'received msg: {msg}')

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
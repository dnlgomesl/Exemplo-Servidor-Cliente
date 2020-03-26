import socket
import threading

class Servidor:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conecctions = []
    def __init__(self):
        self.sock.bind(('localhost', 9999))
        self.sock.listen(1)
        print("Servidor no ar...")

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for conecction in self.conecctions:
                conecction.send(data)
            if not data:
                print(str(a[0]) + ':' + str(a[1]), 'disconnected')
                self.conecctions.remove(c)
                c.close()
                break

    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c,a))
            cThread.daemon = True
            cThread.start()
            self.conecctions.append(c)
            print(str(a[0]) + ':' + str(a[1]), 'connected')

server = Servidor()
server.run()

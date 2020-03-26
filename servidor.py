import socket
import threading

class Servidor:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sock.bind(('localhost', 9999))
        self.sock.listen(1)
        print("Servidor no ar...")

    def customer(self, conn, addr):
        conn.send('Você está conectado'.encode('utf-8'))
        while True:
            data = conn.recv(1024)
            print(data.decode('utf-8')) # não sei se é necessário
            for connection in self.connections:
                connection.send(data)
            if not data:
                print(str(addr[0]) + ':' + str(addr[1]), 'disconnected')
                self.connections.remove(conn)
                conn.close()
                break

    def run(self):
        while True:
            conn, addr = self.sock.accept()
            cThread = threading.Thread(target=self.customer, args=(conn,addr))
            cThread.daemon = True
            cThread.start()
            self.connections.append(conn)
            print(str(addr[0]) + ':' + str(addr[1]), 'connected')

server = Servidor()
server.run()

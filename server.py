import socket
import threading

from game import Game

lock = threading.Lock()
id_counter = 0

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))


def close_server_handler(sig, frame):
    s.close()


open_connections = {}


def broadcast(msg):
    for identifier in open_connections:
        send(identifier, msg)


def send(identifier, msg):
    open_connections[identifier].send(bytearray(msg, "UTF-8"))


game = Game(broadcast, send)


class SessionThread(threading.Thread):
    def __init__(self, connection, player_id) -> None:
        super().__init__()
        self.connection = connection
        self.player_id = player_id

    def run(self) -> None:
        while True:
            data = self.connection.recv(BUFFER_SIZE)
            if not data:
                del open_connections[self.player_id]
                return
            print("received data:", data)
            game.raise_money(self.player_id, 10)


while True:
    s.listen(1)
    conn, address = s.accept()
    print('Connection address:', address)

    lock.acquire()
    client_id = id_counter
    id_counter += 1
    lock.release()

    open_connections[client_id] = conn
    conn.send(bytearray('Your id is ' + str(client_id), "UTF-8"))
    SessionThread(conn, client_id).start()

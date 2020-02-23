import socket
import threading

from game import Game

lock = threading.Lock()
id_counter = 0

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
s.bind((TCP_IP, TCP_PORT))

open_connections = {}
threads = {}
close_sessions = False


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
            if close_sessions:
                break
            try:
                data = self.connection.recv(BUFFER_SIZE)
                if not data:
                    del open_connections[self.player_id]
                    break
                print("received data:", data)
                game.raise_money(self.player_id, 10)
            except socket.timeout:
                pass
            except ConnectionResetError:
                break


while True:
    try:
        s.listen(1)
        new_connection = None
        while True:
            try:
                conn, _ = s.accept()
                new_connection = conn
                new_connection.settimeout(2)
                break
            except socket.timeout:
                continue

        lock.acquire()
        client_id = id_counter
        id_counter += 1
        lock.release()

        open_connections[client_id] = new_connection
        new_connection.send(bytearray('Your id is ' + str(client_id), "UTF-8"))
        thread = SessionThread(new_connection, client_id)
        threads[client_id] = thread
        thread.start()
    except KeyboardInterrupt:
        break

s.close()
close_sessions = True

for t in threads:
    threads[t].join()

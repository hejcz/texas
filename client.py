import socket
import threading

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
s.connect((TCP_IP, TCP_PORT))
reading = True


class Reader(threading.Thread):
    def run(self) -> None:
        while True:
            try:
                if not reading:
                    break
                data = s.recv(BUFFER_SIZE)
                if not data:
                    break
                print(str(data, "UTF-8"))
            except socket.timeout:
                pass
            except ConnectionResetError:
                break


reader = Reader()
start = reader.start()

while True:
    try:
        s.send(bytearray(input(), "UTF-8"))
    except KeyboardInterrupt:
        break

reading = False
reader.join()
s.close()

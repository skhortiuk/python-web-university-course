import socket
import threading

HOST = "127.0.0.1"
PORT = 8001


def client_handler(conn: socket.socket):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"[*] <- {data.decode()}")
        conn.send(data)
        print(f"[*] -> {data.decode()}")


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.bind((HOST, PORT))
connection.listen(1)
print(f"[*] Start listen ad {HOST}:{PORT}")

while True:
    client, addr = connection.accept()
    print(f"[*] New connection from {addr}")
    client_thread = threading.Thread(target=client_handler, args=(client,))
    client_thread.start()

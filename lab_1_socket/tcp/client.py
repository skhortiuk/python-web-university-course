import socket

HOST = '127.0.0.1'
PORT = 8001


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        s.send(input("-> ").encode())

        data = s.recv(1024)
        print(f"<- {data.decode()}")

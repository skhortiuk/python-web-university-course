from socket import socket, AF_INET, SOCK_STREAM
import threading

HOST: str = "127.0.0.1"
PORT: int = 8001
clients: dict = {}


def register_user(connection: socket, address: str):
    while True:
        connection.send(
            "<- [admin] Hello) please choose your username (2-14 "
            "charsets):\n".encode()
        )
        username = connection.recv(1024).decode().rstrip()
        if 2 < len(username) > 14:
            connection.send(
                "<- [admin] Choose another username\n".encode()
            )
            continue
        connection.send(
            f"<- [admin] Hi,{username}, enjoy our "
            f"chat;)\n".encode()
        )
        clients[address] = {"conn": connection, "username": username}
        cast_msg(address, f"Entered the room, say welcome\n")
        return


def cast_msg(address: str, data: str):
    from_username = clients[address]["username"]
    for addr, client in clients.items():
        if addr == address:
            continue

        try:
            client["conn"].send(f"-> [{from_username}] {data}".encode())
        except Exception:
            clients[addr]["conn"].close()


def client_handler(connection: socket, address: str):
    if address not in clients:
        register_user(connection, address)

    while True:
        data = connection.recv(1024).decode()
        if data:
            cast_msg(address, data)


if __name__ == '__main__':
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()
        print(f"[*] Starting listen on {HOST}:{PORT}.")
        while True:
            conn, addr = sock.accept()
            print(f"[*] New connection from {addr}")
            print(f"[*] Now in chat {len(clients)} users.")
            try:
                client_th = threading.Thread(
                    target=client_handler,
                    args=(conn, addr)
                )
                client_th.start()
            except Exception as err:
                print(f"[!] {err}")

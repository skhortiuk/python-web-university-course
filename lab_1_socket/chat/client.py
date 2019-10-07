import select
import socket
import sys

HOST = '127.0.0.1'
PORT = 8001


def prompt():
    sys.stdout.write('-> ')
    sys.stdout.flush()


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    try:
        s.connect((HOST, PORT))
    except Exception:
        sys.exit()

    while 1:
        socket_list = [sys.stdin, s]

        read_sockets, _, _ = select.select(socket_list, [], [])

        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096).decode()
                if not data:
                    sys.exit()
                else:
                    sys.stdout.write(f"\r{data}")
                    prompt()

            else:
                msg = sys.stdin.readline()
                s.send(msg.encode())
                prompt()

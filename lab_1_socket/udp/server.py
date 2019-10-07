from socket import socket, AF_INET, SOCK_DGRAM


HOST = "127.0.0.1"
PORT = 8001

s = socket(AF_INET, SOCK_DGRAM)

s.bind((HOST, PORT))
print(f"[*] Start listen ad {HOST}:{PORT}")

while True:
    data, addr = s.recvfrom(1024)
    print(f"[*] Received {data.decode()} from {addr}")

    if not data or data.decode() == "break":
        break

    reply = 'OK...' + data.decode()
    s.sendto(reply.encode(), addr)

s.close()

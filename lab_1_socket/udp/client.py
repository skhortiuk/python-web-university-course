from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)

host = '127.0.0.1'
port = 8001

while True:
    s.sendto(input('-> ').encode(), (host, port))
    data, addr = s.recvfrom(1024)
    print(f"<- {data.decode()}")

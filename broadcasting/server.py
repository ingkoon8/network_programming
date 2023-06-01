import socket

s_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 브로드캐스틩은 UDP 소켓에서만 가능
s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # SOL_SOCKET level에서 사용, 소켓 재사용을 위해 SO_REUSEADDR
s_sock.bind(('',2500))

while 1:
    msg, addr = s_sock.recvfrom(1024)
    print(msg, addr)

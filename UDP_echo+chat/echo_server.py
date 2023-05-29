import socket

s_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP 소켓
s_sock.bind(('', 2500))
print('Waiting for connection...')

while 1:
    data, addr = s_sock.recvfrom(1024) # 데이터와 상대방 종단점 주소 수신
    print('Receive from ',addr)
    print('Received message : ', data.decode())
    s_sock.sendto(data, addr)

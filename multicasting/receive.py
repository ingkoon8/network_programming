import socket, struct

group_addr = '224.0.0.255'
r_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
r_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
r_sock.bind(('',2500))

# 가입할 그룹 주소는 바이너리로 표시되어야 하므로 10진 표기법 주소를 압축형 바이너리 주소로 변환
mreq = struct.pack('4sl', socket.inet_aton(group_addr), socket.INADDR_ANY) 

r_sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq) # 그룹 가입
print('Ready to receive')

while 1:
    msg, addr = r_sock.recvfrom(1024)
    print('Received {} from ({}, {})'.format(msg.decode(), *addr))
    r_sock.sendto('ACK'.encode(), addr) # ACK 전송

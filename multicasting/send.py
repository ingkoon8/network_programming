import socket, struct

group_addr = ('224.0.0.255', 2500) # 그룹 주소
s_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_sock.settimeout(0.5)

# time to live 설정
TTL = struct.pack('@i', 2) # TTL (=2)을 4 바이트로 표현
# IPPROTO_IP 옵션 사용
s_sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, TTL)

while 1:
    msg =input('Multicast Message : ')
    s_sock.sendto(msg.encode(), group_addr)

    while 1:
        try:
            response, addr = s_sock.recvfrom(1024)
        except socket.timeout:
            break
        else:
            print('{} from {}'.format(response.decode(), addr))

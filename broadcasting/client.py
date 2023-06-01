import socket

addr = ('192.168.64.255', 2500)
#addr = ('<broadcast>', 2500) # 브로드캐스트 주소를 모를 때 사용 가능

c_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
c_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # 브로드캐스트 옵션 설정

while 1:
    msg = input('Broadcast Message : ')
    c_sock.sendto(msg.encode(), addr)

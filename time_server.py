import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server=('', 8010) # 종단점 주소
sock.bind(server) # 주소와 소켓 결합
sock.listen(5) # 최대 동시 5개 연결가능, 연결 대기

while True:
    client,addr = sock.accept() # 연결 허용, 클라이언트 소켓과 주소 반환 (ip, port)
    print('Connection requested from', addr)
    client.send(time.ctime(time.time()).encode()) # time server program, bytes형 메시지 전송
    client.close()

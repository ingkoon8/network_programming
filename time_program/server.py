import socket
import time
n=0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server=('', 8030) # 종단점 주소
sock.bind(server) # 주소와 소켓 결합
sock.listen(5) # 최대 동시 5개 연결가능, 연결 대기

while True:
    client,addr = sock.accept() # 연결 허용, 클라이언트 소켓과 주소 반환 (ip, port)
    print('Connection requested from', addr)
    string = client.recv(1024).decode()
    if string != None: # 몇번째 접속자인지 카운트
        n+=1
    string2=str(n)
    client.send(string2.encode())
    client.recv(1024) # 딜레이
    client.send(time.ctime(time.time()).encode()) # time server program, bytes형 메시지 전송
    client.close()

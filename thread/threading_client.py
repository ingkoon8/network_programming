import socket
import threading

def send(s):
    while 1:
        msg = input()
        s.send(msg.encode())

def receive(s):
    while 1:
        msg = s.recv(1024)
        print(f'Received message : {msg.decode()}')


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 서버 주소 입력
    serverIp = input(('Server IP(default : 127.0.0.1): '))
    if serverIp == '':
        serverIp = '127.0.0.1'
    # 포트 입력
    port = input('port(default : 2500) : ')
    if port == '':
        port = 2500
    else:
        port=int(port)

    s.connect((serverIp, port))
    print('Connected to ' + serverIp)

    Thread1 = threading.Thread(target = send, args = (s,)) # 서브스레드 생성
    Thread1.start()

    Thread2 = threading.Thread(target = receive, args = (s,)) # 서브스레드 생성
    Thread2.start()
    

    

import random
import socket

c_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c_sock.connect(('localhost', 2500))

for i in range(10):
    delay = 1.0 # 딜레이는 0.1초부터 시작
    data = input('Sending message : ')

    while 1:
        c_sock.send(data.encode())
        print(f'Waiting up to {delay} seconds for a reply')
        c_sock.settimeout(delay) # 타임아웃 설정
        try:
            data = c_sock.recv(1024)
        except socket.timeout:
            delay *= 2 # 딜레이 두배씩 증가
            if delay > 2.0:
                print('disconnect from server')
                break
        else:
            print('Response : ', data.decode())
            break

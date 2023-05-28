import socket

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

while True:
    msg = input('Sending message : ')

    if not msg:
        continue
    try:
        s.send(msg.encode())
    except:
        print('연결 종료')
        break
    s.settimeout(1.0) # 메세지를 수신받는 타임 아웃을 1초로 설정
    try:
        msg = s.recv(1024)
        if not msg:
            print('연결 종료')
            break
        print(f'Received message : {msg.decode()}')
    except s.timeout: # 타임 아웃 발생시
        pass
    except:
        print('연결 종료')
        break
s.close()

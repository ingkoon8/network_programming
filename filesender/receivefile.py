import socket

s_sock = socket.socket()
host = 'localhost'
port = 2500

s_sock.connect((host, port))
s_sock.send('Ready'.encode())
fn = s_sock.recv(1024).decode()

with open('/Users/yujaemin/Desktop/python/network2/'+fn, 'wb') as f: # 전송 받을 path 지정
    print('file opened')
    print('receiving file...')
    while 1:
        data = s_sock.recv(8192) # 파일 내용 수신
        if not data:
            break
        f.write(data) # 내용을 파일에 쓰기
print('Download complete')
s_sock.close()
print('Connection closed')

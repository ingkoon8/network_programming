import socket

s_sock = socket.socket()
host = 'localhost'
port = 2500

s_sock.connect((host, port))
s_sock.send('Ready'.encode())
fn = s_sock.recv(1024).decode()

with open('/Users/yujaemin/Desktop/python/network2/'+fn, 'wb') as f: # 보낼 path 지정
    print('file opened')
    print('receiving file...')
    while 1:
        data = s_sock.recv(8192)
        if not data:
            break
        f.write(data)
print('Download complete')
s_sock.close()
print('Connection closed')

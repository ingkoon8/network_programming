from socket import *

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
print('Waiting for clients...')

c_sock, (r_host, r_port) = sock.accept()
print('connected by', r_host, r_port)

while True:
    try:
        data = c_sock.recv(BUFSIZE)
        if not data:
            print('연결 종료')
            c_sock.close() # 연결 종료
            break
    except: # error 발생 
        print('연결 종료')
        c_sock.close()
        break
    else: # 정상적으로 수신
        print('Received Message : ', data.decode())
    
    try:
        c_sock.send(data)
    except: # 연결 종료로 인한 error
        print('연결 종료')
        c_sock.close()
        break

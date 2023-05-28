from socket import *

port = 2500
BUFSIZE = 1024
table = { '1' : 'one', '2' : 'two', '3':'three', '4':'four', '5':'five',
         '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten'}

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
print('Waiting for clients...')

c_sock, (r_host, r_port) = sock.accept()
print('connected by', r_host, r_port)

while True:
    try:
        data = c_sock.recv(BUFSIZE).decode()
        msg = table[data]
        c_sock.send(msg.encode())
        if not data:
            print('연결 종료')
            c_sock.close() # 연결 종료
            break
    except: # error 발생 
        c_sock.send('Try again'.encode())
    
    

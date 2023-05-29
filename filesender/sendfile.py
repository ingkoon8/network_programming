import socket
import sys

port = 2500
s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.bind(('', port))
s_sock.listen(1)

print('Waiting for connection...')

c_sock, c_addr = s_sock.accept()
print('Connected from ', c_addr)
msg = c_sock.recv(1024)
print(msg.decode())

filename = input('File name to send : ')
print(f"Sending '{filename}'")

fn = filename.split('/')

c_sock.sendall(fn[-1].encode()) # path를 제외하고 파일 이름만 전송

with open(filename, 'rb') as f:
    c_sock.sendfile(f,0)

print('Sending complete')

c_sock.close()

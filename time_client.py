import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8010))
print('현재 시각 : ',sock.recv(1024).decode()) # 한 번에 수신할 수 있는 최대 바이트 수 1024로 설정
sock.close()

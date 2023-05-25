import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8030))
string = '서버 접속'
sock.send(string.encode())
data= sock.recv(1024) # 한 번에 수신할 수 있는 최대 바이트 수 1024로 설정
print('당신은 ',data.decode(),'번째 접속자입니다.') 
sock.send('delay'.encode()) # 딜레이
data2=sock.recv(1024)
print('현재 시각 : ', data2.decode())

sock.close()

import random
import socket

s_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_sock.bind(('', 2500))

print('Waiting for connection...')

while 1:
    data, c_addr = s_sock.recvfrom(1024)
    if random.randint(1,10) < 4: # 4미만의 숫자가 나오면 전송 손실이 일어났다고 가정
        print(f'Packet form {c_addr} lost!')
        continue
    print(f'Message is {data.decode() !r} from {c_addr}')

    s_sock.sendto('ACK'.encode(),c_addr) # ACK 응답 전송

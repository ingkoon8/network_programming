import socket

c_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = input('Sending message : ')
c_sock.sendto(msg.encode(), ('localhost', 2500))
while 1:
    data, addr = c_sock.recvfrom(1024)
    print()
    print('Receive from ',addr)
    print('Received message : ', data.decode())
    print()
    msg = input('Sending message : ')
    c_sock.sendto(msg.encode(), ('localhost', 2500))

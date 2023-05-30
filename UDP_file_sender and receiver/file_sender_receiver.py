import socket, time, sys

BUFSIZE = 1024*8

def Receiver():
    sock.bind(addr)

    file_name, client = sock.recvfrom(BUFSIZE)
    sock.sendto('ACK'.encode(), client) # 데이터를 정상적으로 수신하면 ACK 응답
    f=(file_name.decode()).split('/')
    with open('/Users/yujaemin/Desktop/python/network2/'+f[-1], 'wb') as fp:
        print('파일 수신중...')
        while 1:
            data = sock.recvfrom(BUFSIZE)
            if not data[0]: # recvfrom은 data(0)와 client(1)의 주소를 반환
                break
            fp.write(data[0])

    print('수신 완료')

def Sender():
    file_name = input('File name to send : ')
    sock.sendto(file_name.encode(), addr)
    resp, client = sock.recvfrom(BUFSIZE)

    if resp.decode() == 'ACK':
        print('ACK')
        fp = open(file_name, 'rb')
        data = fp.read(BUFSIZE)
        print('송신중...')

        while data:
            sock.sendto(data, client)
            time.sleep(0.02) # 수신자가 저장할 때까지 대기
            data =fp.read(BUFSIZE)

        sock.sendto(data, client) # 파일 내용을 바이너리로 읽기 때문에 인코딩 필요 없음
        fp.close()
        print('전송완료')
    else:
        print('수신 응답 오류')


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ('localhost', 2500)

    
    role = sys.argv[1] # 's' = 송신, 'r' = 수신
    if role == 's':
        Sender()
    elif role == 'r':
        Receiver()
    else:
        print('s(송신) 또는 r(수신)을 지정하세요')
    

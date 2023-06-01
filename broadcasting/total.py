# 서버 total.py server ""
# 클라이언트 total.py client 브로드캐스팅 할 호스트 IP

import argparse, socket
BUFSIZE = 1024

def client(network, port):
    c_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    c_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # 브로드캐스트 옵션 설정
    text = input('Broadcast Message : ')
    c_sock.sendto(text.encode(), (network, port))

def server(interface, port):
    s_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s_sock.bind((interface, port))
    print('{}에서 수신 대기 중'.format(s_sock.getsockname()))
    while 1:
        data, address = s_sock.recvfrom(BUFSIZE)
        text = data.decode()
        print('클라이언트 ({})의 브로드캐스팅 메세지 : {!r}'.format(address, text))

if __name__ == '__main__':
    role = {'client' : client, 'server' : server}

    # 명령 인수 처리
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=role)
    parser.add_argument('host')
    parser.add_argument('-p', type =int, default=1060)
    args = parser.parse_args()

    function = role[args.mode]
    function(args.host, args.p)

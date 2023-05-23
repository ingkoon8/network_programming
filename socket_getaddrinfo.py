import socket
def get_constants(prefix):
    return { getattr(socket, n):n # 속성값 : 속성 문자
            for n in dir(socket) # socket의 속성 문자
            if n.startswith(prefix) # prefix로 시작하는 속성 문자 조사
            }
families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

for response in socket.getaddrinfo('www.naver.com','http'):

    family, socktype, proto, canoname, sockaddr = response
    print('Family :',families[family])
    print('Type :',types[socktype])
    print('Protocol :',protocols[proto])
    print('Canonical name :',canoname)
    print('Socket address :',sockaddr)
    print()

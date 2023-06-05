import socket, _thread

def handler(c_sock, addr): # 클라이언트가 접속을 할 때마다 생성
    while 1:
        data = c_sock.recv(1024)
        if not data:
            break
        print(f'receive from {addr} : ' + data.decode()) 
        wriete_handle(c_sock, addr)
        

def wriete_handle(c_sock, addr): # 메세지를 보내는 함수
    msg=input('sending message : ')
    c_sock.send(msg.encode())
    print(f'send to {addr} : '+ msg)


if __name__ == '__main__':
    s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s_sock.bind(('', 2500))
    s_sock.listen(5)

    while 1:
        print('Waiting for connection...')
        c_sock, addr = s_sock.accept()
        print('connected from', addr)
        _thread.start_new_thread(handler, (c_sock, addr)) # 클라이언트가 접속할 때마다 새로운 스레드 생성

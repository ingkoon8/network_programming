import socket
import threading

def handler(c_sock, addr):
    global connections
    while 1:
        try:
            data = c_sock.recv(1024)
            if not data:
                connections.remove(c_sock)
                c_sock.close()
                continue
        except:
            continue

        for connection in connections:
            try:
                connection.send(bytes(data)) # 연결된 모든 클라이언트에게 전송
            except:
                continue

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('',2500))
sock.listen(1)
connections = []
print('Ready for connection...')

while 1:
    c_sock, addr = sock.accept()
    connections.append(c_sock)
    cThread = threading.Thread(target = handler, args = (c_sock,addr)) # 서브스레드 생성
    cThread.daemon = True # 메인스레드가 종료되면 서브스레드도 종료
    cThread.start()

    print('연결된 클라이언트 : ', connections)

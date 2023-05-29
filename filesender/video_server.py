import socket, cv2, pickle, struct, imutils

s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.bind(('', 2500))
s_socket.listen(1)

print('Waiting for connection...')

while 1:
    c_socket, c_addr = s_socket.accept()
    print('Connected from ',c_addr)
    if c_socket:
        vid = cv2.VideoCapture(0) # 웹 카메라
        if vid.isOpened():
            print('width : {}, height : {}'.format(vid.get(3), vid.get(4)))
        while (vid.isOpened()):
            img, frame= vid.read() # 프레임 획득
            frame = imutils.resize(frame, width=640) # 프레임 크기 조절
            frame_bytes = pickle.dumps(frame) # 프레임을 바이트 스트림으로 변환
            message = struct.pack('Q', len(frame_bytes)) + frame_bytes # 메세지 = [frame 길이(unsigned 8bytes) +frame]
            c_socket.sendall(message)

            cv2.imshow('Server Video', frame) # 전송영상 표시
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                c_socket.close()

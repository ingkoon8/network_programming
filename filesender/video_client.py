import socket, cv2, pickle, struct

c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c_socket.connect(('localhost', 2500))
data = b''
payload_size = struct.calcsize('Q') # 길이 정보를 unsigned 8bytes로 표시

while 1:
    while len(data) < payload_size: # 수신 프레임은 길이 영역보다 커야함
        packet = c_socket.recv(4*1024)
        if not packet:
            break
        data += packet

    packed_msg_size = data[:payload_size] # 프레임 길이 추출
    data = data[payload_size:] # 프레임 추출
    msg_size = struct.unpack("Q",packed_msg_size)[0] # 프레임 길이를 파이썬 자료형으로 변환

    while len(data) < msg_size: # 길이 만큼의 프레임 수신
        data += c_socket.recv(4*1024)
    frame_data = data[:msg_size] # 한 프레임 크기를 잘라냄
    data = data[msg_size:] # 다음 프레임

    # 동영상 프레임 표시
    frame = pickle.loads(frame_data) # 바이트 스트림을 프레임으로 변환
    cv2.imshow('Client Video', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
c_socket.close()

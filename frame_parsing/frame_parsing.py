import socket
import capsule

SIZE = 5 # 페이로드 크기
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP 소켓
sock.setblocking(True) # 블로킹모드
sock.settimeout(0.1) # 타임아웃 0.1초
sock.connect(('localhost', 2500))

# header 구성
header = {"START":0x05, "Address":1, "seqNo":1, "LENGTH":SIZE}
header_size = 11 # 시작문자 1, 주소 2, 시퀀스넘버:4, 길이:4

frame_seq="" # 전송 프레임
msg=input('sending message : ')

for i in range(0, len(msg), SIZE):
    start = i
    frame_seq += capsule.frame(header["START"], header["Address"], header["seqNo"], msg[start:start+SIZE])
    start += SIZE
    header["seqNo"] += 1

sock.send(frame_seq.encode())

r_msg = '' # 수신 메세지
seq_num = 1
while 1:
    try:
        if sock.recv(1).decode() == chr(0x05): # 프레임 시작
            p_msg = sock.recv(header_size-1).decode() # 시작문자를 제외한 모든 헤더

            if int(p_msg[2:6]) == seq_num: # 시퀀스 넘버 확인
                payload_len = int(p_msg[-4:]) # payload 길이
                r_msg = r_msg + sock.recv(payload_len).decode()

    except:
        break

print('복원 메세지 : ', r_msg)
sock.close()

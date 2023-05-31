def frame(start_ch, addr, seqNo, msg): # 프레임 구성 함수
    return f'{start_ch:c}{addr:02d}{seqNo:04d}{len(msg):04d}{msg}'

if __name__ == '__main__':
    start_ch = 0x05 # 시작문자
    addr = 2 # 주소
    seqNo = 1 # 시퀀스 넘버

    msg = input('sending message : ')

    capsule = frame(start_ch, addr, seqNo, msg)
    print(capsule)

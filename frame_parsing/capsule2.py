start_ch = 0x05 # 시작문자
addr = 2 # 주소
seqNo = 1 # 시퀀스 넘버
msg = input('sending message : ')
frame={"start":start_ch, "address":addr, "Seq_no":seqNo, "length":len, "payload":msg}
print(f'{frame["start"]:c} {frame["address"]:02d} {frame["Seq_no"]:04d} {frame["length"](msg):04d} {frame["payload"]}')

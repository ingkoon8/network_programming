frame = []
msg = input('sending message : ')
size = 4

for i in range(0,len(msg),4):
    frame.append(msg[i:i+size])
print('단편화 메세지 : {}'.format(frame))
print('재조립 메세지 : {}'.format(''.join(frame)))

import socket
HOSTS = [ 'www.naver.com', 'www.google.com', 'www.python.org','testname']

for host in HOSTS:
    print(host)
    try:
       hostname, aliases, addresses = socket.gethostbyname_ex(host)
       print('Hostname : ',hostname)
       print('Aliases : ',aliases)
       print('Addresses : ',addresses)
    # host 찾을 수 없을 경우 error
    except socket.error as e_msg:
        print('{} : {}'.format(host, e_msg))
    print()

# 나의 host 정보 가져오기
myhost = socket.gethostname()
print(socket.gethostbyname_ex(myhost))

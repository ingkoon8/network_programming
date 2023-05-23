from socket import *
HOSTS = [ 'www.naver.com', 'www.google.com', 'www.python.org','testname']

for host in HOSTS:
    print(host)
    try:
       hostname, aliases, addresses = gethostbyname_ex(host)
       print('Hostname : ',hostname)
       print('Aliases : ',aliases)
       print('Addresses : ',addresses)
    # host 찾을 수 없을 경우 error
    except error as e_msg:
        print('{} : {}'.format(host, e_msg))
    print()

# 나의 host 정보 가져오기
myhost = gethostname()
print(gethostbyname_ex(myhost))

# 완전한 도메인 확인
print(getfqdn('pymotw.com'))

# ip 주소로 호스트 정보 가져오기
hostname2, aliases2, addresses2 = gethostbyaddr('203.249.39.46')
print('Hostname : ',hostname2)
print('Aliases : ',aliases2)
print('Addresses : ',addresses2)

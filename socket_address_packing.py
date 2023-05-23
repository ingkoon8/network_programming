import binascii
import socket

#IPv4
for string_address in ['203.249.39.46', '127.0.0.1']:
    packed = socket.inet_aton(string_address) #IPv4 문자열 주소를 압축 바이너리 형식으로 변환
    print('Original : ',string_address)
    print('Packed : ',binascii.hexlify(packed)) #2진수 주소를 16진수 주소로 변환
    print('Unpacked : ',socket.inet_ntoa(packed)) #2진수 주소를 문자열 주소로 변환
    print()

#IPv6
string_address2 = '2002:ac10:10a:1234:21e:52ff:fe74:40e'

packed2 = socket.inet_pton(socket.AF_INET6, string_address2) #IPv6 문자열 주소를 압축 바이너리 형식으로 변환
print('Original : ',string_address2)
print('Packed : ',binascii.hexlify(packed2)) #2진수 주소를 16진수 주소로 변환
print('Unpacked : ',socket.inet_ntop(socket.AF_INET6, packed2)) #2진수 주소를 문자열 주소로 변환

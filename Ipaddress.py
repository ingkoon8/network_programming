import binascii
import ipaddress as ipa

Address = ['192.168.0.5', '2001:0:9d38:6abd:480:f1f:3f57:fffb']

for ipaddr in Address:
    addr = ipa.ip_address(ipaddr)
    print(f'IP address : {addr!r}') 
    print('IP version : ',addr.version)
    print('Packed addr : ',binascii.hexlify(addr.packed)) # 16진수로 표현
    print('Integer addr : ',int(addr))
    print('Is private? : ',addr.is_private) # 사설 네트워크인지 확인
    print()

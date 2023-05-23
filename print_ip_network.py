import ipaddress as ipa
print(ipa.ip_network('192.0.2.0/24'))
print(ipa.ip_network('2001:db8::0/96'))
print(ipa.ip_network('192.0.2.0/24').with_netmask)
print(ipa.ip_network('2001:db8::0/96').with_netmask)
print(ipa.ip_network('192.0.2.0/24').with_hostmask)
print(ipa.ip_network('2001:db8::0/96').with_hostmask)

# 네트워크 내의 개별 주소
net4=ipa.ip_network('192.0.2.0/24')
print(net4.num_addresses)
net6=ipa.ip_network('2001:db8::0/96')
print(net6.num_addresses)

# 0과 255는 호스트로 사용 불가
for x in net4.hosts():
    print(x)

# 넷 마스크와 호스트 마스크
print(net4.netmask)
print(net4.hostmask)
print(net6.netmask)
print(net6.hostmask)


import ipaddress
print(ipaddress.ip_address('192.0.2.1'))
print(int(ipaddress.ip_address('2001:DB8::1')))
print(ipaddress.ip_address(3221225985))
print(ipaddress.IPv4Address(1))
print(ipaddress.IPv6Address(1))

addr = ipaddress.ip_address('127.0.0.1')
print(addr.is_loopback)
print(addr.version)

import ipaddress as ipa
print(ipa.ip_interface('192.0.2.1/24'))
print(ipa.ip_interface('2001:db8::1/96'))

interface = ipa.IPv4Interface('192.168.0.5/24')
print(interface.ip)
print(interface.network)

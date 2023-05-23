import ipaddress as ipa
print(ipa.ip_network('192.0.2.0/24'))
print(ipa.ip_network('2001:db8::0/96'))
print(ipa.ip_network('192.0.2.0/24').with_netmask)
print(ipa.ip_network('2001:db8::0/96').with_netmask)
print(ipa.ip_network('192.0.2.0/24').with_hostmask)
print(ipa.ip_network('2001:db8::0/96').with_hostmask)

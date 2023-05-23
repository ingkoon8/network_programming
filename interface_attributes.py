import ipaddress as ipa

ADDRESSES = ['10.9.0.6/24', 'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa/64']

for ip in ADDRESSES:
    iface = ipa.ip_interface(ip)
    print('{!r}'.format(iface))
    print('network : \n',iface.network)
    print('ip : \n',iface.ip)
    print('IP with predixlen : \n',iface.with_prefixlen)
    print('netmask : \n',iface.with_netmask)
    print('hostmask : \n',iface.with_hostmask)
    print()

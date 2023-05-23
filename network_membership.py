import ipaddress as ipa

NETWORKS = [ipa.ip_network('10.9.0.0/24'), ipa.ip_network('fdfd:87b5:b475:5e3e::/64')]
ADDRESSES = [ipa.ip_address('10.9.0.6'), ipa.ip_address('10.7.0.31'), ipa.ip_address('fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa'),
             ipa.ip_address('fe80::3840:c439:b25e:63b0')]

for ip in ADDRESSES:
    for net in NETWORKS:
        if ip in net:
            print('{}is on {}'.format(ip, net))
            break
    else:
        print('{}is not on a known netwrok'.format(ip))
    print()

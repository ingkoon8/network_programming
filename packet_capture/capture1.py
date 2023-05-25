import pcap
import re
import dpkt
import socket

sniffer = pcap.pcap(name=None,promisc=True,immediate=True,timeout_ms=50) # name=eth, None 일경우 모든 default / promisc는 모든 eth에서 패킷 수집 
sniffer.setfilter('tcp and port 80') # set packet filter

for t, p in sniffer:
    eth = dpkt.ethernet.Ethernet(p)
    ip = eth.data
    tcp = ip.data
    try:
        if len(tcp.data) > 0:
            req = dpkt.http.Request(tcp.data)	#Request패킷만 추출
            print("----------------------------------------------------------------")
            print(req)	# 패킷 출력
            print("----------------------------------------------------------------")
    except:
        pass

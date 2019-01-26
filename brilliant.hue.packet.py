import socket
msg = \
'M-SEARCH * HTTP/1.1\r\n'\
'MX: 5\r\n'\
'ST: upnp:rootdevice\r\n'\
'MAN: "ssdp:discover"\r\n'\
'User-Agent: UPnP/1.0 DLNADOC/1.50 Platinum/1.0.5.13\r\n\r\n'\

# Set up UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.settimeout(2)
s.sendto(msg, ('239.255.255.250', 1900) )

try:
    while True:
        data, addr = s.recvfrom(65507)
        print addr, data
except socket.timeout as e:
    print e

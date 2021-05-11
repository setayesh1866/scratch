import scapy.all as scapy


s = scapy

s.Ether().show()
s.IP().show()
s.TCP().show()
s.UDP().show()
s.PPP().show()
s.ARP().show()


counter = 0

while True:
    e = s.Ether()
    i = s.IP(src="192.168.100.15", dst="192.168.100." + str(counter))
    t = s.TCP(sport=700, dport=22)
    counter += 1
    s.sendp(e/i/t)
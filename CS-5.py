#Saving and Reading Packets
from scapy.all import sniff, IP, wrpcap, rdpcap

packets = sniff(count=10)
wrpcap("packets.pcap", packets)

# Read packets from a file
saved_packets = rdpcap("packets.pcap")
for packet in saved_packets:
    print(packet.summary())

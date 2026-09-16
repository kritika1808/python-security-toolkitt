import scapy.all as scapy
def show_packet(packet):
    if packet.haslayer(scapy.IP):
        src = packet[scapy.IP].src
        dst = packet[scapy.IP].dst
        proto = packet[scapy.IP].proto
        print(f"{src} -> {dst} | Protocol:{proto}")
def run_packet_sniffer():
    interface = input("Enter network interface: ").strip()
    count = int(input("Enter number of packets:"))
    print(f"capturing{count} packets on {interface}...")
    scapy.sniff(iface=interface,count=count,prn=show_packet,store=False)
    print("[+] Packet capture completed.")
if __name__ == "__main__":run_packet_sniffer()

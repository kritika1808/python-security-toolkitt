import scapy.all as scapy

def scan_network(target):
    print("Scanning:", target)
    arp=scapy.ARP(pdst=target)
    broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    request = broadcast / arp
    answered, unanswered = scapy.srp(request,timeout=2, verbose=False)
    for sent, received in answered:
        print(received.psrc, received.hwsrc)

def run_scanner():
    target = input("Enter authorized network/range:").strip()
    scan_network(target)

if __name__ == "__main__":
    run_scanner()

import scapy.all as scapy
def run_arp_spoofer():
    interface = input("Enter network interface: ").strip()
    target_ip = input("Enter authorized target IP: ").strip()
    print(f"\nInterface:{interface}")
    print(f"Authorized target:{target_ip}")
    arp_request = scapy.ARP(pdst=target_ip)
    print("[+] ARP request created successfully.")
    print(f"[+] Target:{arp_request.pdst}")
    print("[+] No spoofed packet was sent.")
if __name__ == "__main__":run_arp_spoofer()    

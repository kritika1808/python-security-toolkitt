import scapy.all as scapy
def run_dns_spoofer():
    domain = input("Enter authorized domain:").strip()
    fake_ip = input ("Enter demonstration IP: ").strip()
    print(f"\nDomain: {domain}")
    print(f"Demonstration IP:{fake_ip}")
    dns_response = scapy.DNSRR(rrname=domain,type="A",rdata=fake_ip)
    print("[+] DNS response record created successfully.")
    print(f"[+] {domain} -> {fake_ip}")
    print("[+] No DNS packet was sent.")
if __name__ =="__main__":run_dns_spoofer()

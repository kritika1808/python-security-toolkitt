from modules.network_scanner import scan_network
from modules.mac_changer import run_mac_changer
from modules.arp_spoofer import run_arp_spoofer
from modules.packet_sniffer import run_packet_sniffer
from modules.network_jammer import run_network_jammer
from modules.dns_spoofer import run_dns_spoofer
from modules.arp_spoof_detector import run_arp_spoof_detector
def show_menu():
   print(" 1. Mac changer")
   print(" 2. Network Scanner")
   print(" 3. ARP Spoofer")
   print(" 4. Packet Sniffer")
   print(" 5. Network Jammer")
   print(" 6. DNS Spoofer")
   print(" 7. ARP Spoof Dectection")
   print(" 0. Exit")
   print("=" * 40)
   print("PYTHON SECURITY TOOLKIT")
   print("=" * 40)

while True:
    show_menu()
    choice = input("Enter your choice:").strip()
    if choice == "1":
        run_mac_changer()
    elif choice =="2":
        target = input ("Enter authorized network/range: ").strip()
        scan_network(target)
    elif choice == "3":
        run_arp_spoofer()
    elif choice =="4":
        run_packet_sniffer()
    elif choice =="5":
        run_network_jammer()
    elif choice =="6":
        run_dns_spoofer()
    elif choice =="7":
        run_arp_spoof_detector()
    elif choice =="0":
        print("Exiting toolkit.")
        break
    else:
        print("Invaild choice.")

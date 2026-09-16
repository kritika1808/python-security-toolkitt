import subprocess

def run_arp_spoof_detector():
    print("Checking ARP table...\n")
    result = subprocess.run(
        ["ip","neigh","show"],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    print("[+] ARP table check completed.")
    print("[+] Review IP-to-MAC mappings for unexpected changes.")

if __name__ == "__main__":
    run_arp_spoof_detector()

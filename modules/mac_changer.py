import subprocess

def change_mac(interface, new_mac):
    try:
        subprocess.run(["sudo","ip","link","set", interface, "down"],
            check=True)
        subprocess.run(["sudo","ip","link","set","dev",  interface, "address", new_mac],
            check=True)
        subprocess.run(["sudo","ip","link","set", interface, "up"],
            check=True)
        print("[+] MAC address changed successfully.")
    except subprocess.CalledProcessError:
        print("[-] Failed to change MAC address.")


def run_mac_changer():
    interface = input("Enter network interface: ").strip()
    new_mac = input("Enter new MAC address: ").strip()
    change_mac(interface, new_mac)
if __name__ == "__main__":
    run_mac_changer()

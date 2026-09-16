
# Python Security Toolkit: An Integrated Ethical Hacking Framework

## Project Overview

**Python Security Toolkit: An Integrated Ethical Hacking Framework** is a beginner-friendly Python-based cybersecurity toolkit developed and tested in a Kali Linux lab environment.

The project combines multiple security-related modules into a single menu-driven program. It provides practical experience with Python, Linux networking, Scapy, network scanning, packet analysis, MAC addresses, ARP, and DNS concepts.

**Project Folder:** `python-security-toolkit`

## Objectives

* Practice Python programming for cybersecurity.
* Understand basic network-security concepts.
* Work with network interfaces, IP addresses, and MAC addresses.
* Perform network scanning in an authorized lab environment.
* Capture and inspect basic network packets.
* Understand ARP and DNS security concepts.
* Develop a modular cybersecurity toolkit.
* Practice safe and ethical security testing.

## Features

| No. | Module              | Purpose                                                            |
| --- | ------------------- | ------------------------------------------------------------------ |
| 1   | MAC Changer         | Changes the MAC address of a selected network interface.           |
| 2   | Network Scanner     | Discovers devices on an authorized network/range using ARP.        |
| 3   | ARP Spoofer         | Demonstrates ARP request creation without sending spoofed packets. |
| 4   | Packet Sniffer      | Captures and displays basic information from IP packets.           |
| 5   | Network Jammer      | Provides a safe simulation of the network-jamming concept.         |
| 6   | DNS Spoofer         | Demonstrates DNS response record creation without sending it.      |
| 7   | ARP Spoof Detection | Displays the ARP table for reviewing IP-to-MAC mappings.           |

## Technologies Used

* Python 3
* Kali Linux
* Scapy
* Linux networking commands
* VirtualBox
* Git and GitHub

## Project Structure

```text
python-security-toolkit/
│
├── .gitignore
├── README.md
├── main.py
├── requirements.txt
│
├── modules/
│   ├── __init__.py
│   ├── arp_spoof_detector.py
│   ├── arp_spoofer.py
│   ├── dns_spoofer.py
│   ├── mac_changer.py
│   ├── network_jammer.py
│   ├── network_scanner.py
│   └── packet_sniffer.py
│
├── screenshots/

```

## Requirements

* Kali Linux
* Python 3
* Scapy
* Network interface available in the lab environment
* Authorization to test the selected network or system

## Installation

Navigate to the project directory:

```bash
cd ~/python-security-toolkit
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

## Running the Toolkit

Run the main program:

```bash
sudo python3 main.py
```

The toolkit provides the following menu:

```text
1. Mac changer
2. Network Scanner
3. ARP Spoofer
4. Packet Sniffer
5. Network Jammer
6. DNS Spoofing
7. ARP Spoof Detection
0. Exit
```

## Module Details

### 1. MAC Changer

The MAC Changer accepts a network interface and a new MAC address.

It uses Linux `ip link` commands to:

1. Bring the interface down.
2. Change the MAC address.
3. Bring the interface back up.

### 2. Network Scanner

The Network Scanner uses Scapy and ARP requests to discover devices on an authorized network or IP range.

It displays:

* IP address
* MAC address

Example network format:

```text
10.0.0.0/24
```

Only authorized networks should be scanned.

### 3. ARP Spoofer

The ARP Spoofer is implemented as a safe educational demonstration.

It:

* Accepts a network interface.
* Accepts an authorized target IP.
* Creates an ARP request.
* Displays the target information.

**No spoofed ARP packet is sent.**

### 4. Packet Sniffer

The Packet Sniffer uses Scapy to capture packets from a selected network interface.

For IP packets, it displays:

* Source IP address
* Destination IP address
* IP protocol number

Example output format:

```text
10.0.0.2 -> 10.0.0.1 | Protocol: 1
```

Packet capture should only be performed on an authorized network or lab environment.

### 5. Network Jammer

The Network Jammer module provides a safe simulation of the concept of network jamming.

It accepts:

* Network interface
* Authorized target

The module only displays simulation information.

**No packets are sent and no network disruption is performed.**

### 6. DNS Spoofer

The DNS Spoofer demonstrates how a DNS response record can be created using Scapy.

It accepts:

* Domain name
* Demonstration IP address

Example:

```text
example.com -> 10.0.0.99
```

The DNS record is created only for demonstration.

**No DNS packet is sent.**

### 7. ARP Spoof Detection

The ARP Spoof Detection module checks the system's ARP neighbor table using:

```bash
ip neigh show
```

It displays the current IP-to-MAC mappings.

The information can be reviewed for unexpected changes in ARP mappings.

## Testing

The Python files were checked for syntax errors using:

```bash
python3 -m py_compile main.py modules/*.py
```

The modules were also tested individually through the main toolkit menu in the Kali Linux lab environment.

## Screenshots

Practical testing screenshots are stored in:

```text
[screenshots](./screenshot/)
```

These screenshots provide evidence of the execution and testing of the project modules.

## Learning Outcomes

This project provided practical experience with:

* Python functions and modules
* Menu-driven Python programs
* Python virtual environments
* Kali Linux
* Linux terminal commands
* Network interfaces
* IP addresses
* MAC addresses
* ARP
* DNS concepts
* Network scanning
* Packet sniffing
* Scapy
* Basic ARP monitoring
* Git and GitHub
* Ethical cybersecurity practices

## Ethical Use and Safety

This toolkit is intended for:

* Educational purposes
* Personal cybersecurity labs
* Authorized security testing
* Controlled demonstrations

Only test systems and networks for which you have permission.

The ARP Spoofer, DNS Spoofer, and Network Jammer modules are intentionally implemented as non-disruptive demonstrations:

* No spoofed ARP packets are sent.
* No DNS packets are sent.
* No jamming or network disruption is performed.

## Disclaimer

This project is intended for educational and authorized cybersecurity testing purposes only.

The author is not responsible for misuse of this project.

Always obtain appropriate authorization before performing security testing, network scanning, packet capture, or other security-related activities.

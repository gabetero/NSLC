import subprocess
import re

def scan_arp(subnet, interface):
    print(f"Scanning {subnet} using ARP on interface {interface}...\n")
    seen = set()

    try:
        result = subprocess.run(
            ['sudo', 'arp-scan', '--interface=' + interface, subnet],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stdout.splitlines()

        for line in output:
            if re.match(r'^\d+\.\d+\.\d+\.\d+', line):
                parts = line.split('\t')
                if len(parts) >= 2:
                    ip = parts[0]
                    mac = parts[1]
                    if (ip, mac) not in seen:
                        vendor = parts[2] if len(parts) > 2 else "Unknown"
                        print(f"IP: {ip:<15}  MAC: {mac:<17}  Vendor: {vendor}")
                        seen.add((ip, mac))

    except Exception as e:
        print("Error running arp-scan:", e)

if __name__ == "__main__":
    subnet = "10.191.155.0/18"
    interface = "wlo1"
    scan_arp(subnet, interface)

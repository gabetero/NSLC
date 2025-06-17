import subprocess  # Used to run external commands
import re  # Used for regular expression matching

def scan_arp(subnet, interface):
    print(f"Scanning {subnet} using ARP on interface {interface}...\n")
    seen = set()  # Set to store (IP, MAC) pairs we've already seen (avoid duplicates)

    try:
        # Run the arp-scan command as a subprocess
        result = subprocess.run(
            ['sudo', 'arp-scan', '--interface=' + interface, subnet],  # Command with interface and subnet
            stdout=subprocess.PIPE,  # Capture standard output
            stderr=subprocess.PIPE,  # Capture error output
            text=True  # Output as string (not bytes)
        )

        # Split output into lines
        output = result.stdout.splitlines()

        # Go through each line of arp-scan output
        for line in output:
            # Match lines that start with an IP address
            if re.match(r'^\d+\.\d+\.\d+\.\d+', line):
                parts = line.split('\t')  # Split line by tabs (IP, MAC, Vendor)
                if len(parts) >= 2:
                    ip = parts[0]  # First part is the IP address
                    mac = parts[1]  # Second part is the MAC address
                    if (ip, mac) not in seen:  # Avoid printing duplicates
                        vendor = parts[2] if len(parts) > 2 else "Unknown"  # Vendor info if available
                        print(f"IP: {ip:<15}  MAC: {mac:<17}  Vendor: {vendor}")  # Nicely formatted output
                        seen.add((ip, mac))  # Mark this IP/MAC as seen

    except Exception as e:
        print("Error running arp-scan:", e)  # Handle any unexpected errors

# Run the script only if this file is being executed directly
if __name__ == "__main__":
    subnet = "10.191.155.0/18"  # Set your subnet (in CIDR notation)
    interface = "wlo1"  # Set the network interface (e.g., wlo1 for Wi-Fi)
    scan_arp(subnet, interface)  # Call the scan function

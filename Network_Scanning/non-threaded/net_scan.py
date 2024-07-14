import ipaddress  # Import the ipaddress module for IP address manipulation 

import subprocess  # Import the subprocess module to run external commands 

  

def ping_host(ip): 

    """ 

    Function to ping a host (IP address) to check if it is reachable. 

  

    Parameters: 

    - ip: The IP address (in string format) to ping. 

  

    Returns: 

    - True if the host is reachable (ping successful), False otherwise. 

    """ 

    # Run the 'ping' command with options to send 1 packet ('-c 1') and wait for 1 second ('-W 1') 

    result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE) 

     

    # Check if the 'ping' command returned successfully (return code 0 means success) 

    if result.returncode == 0: 

        return True  # Host is reachable 

    else: 

        return False  # Host is not reachable 

  

def scan_network(subnet): 

    """ 

    Function to scan a network subnet for active hosts. 

  

    Parameters: 

    - subnet: The network subnet (in CIDR notation) to scan, e.g., "192.168.1.0/24". 

  

    This function iterates through all IP addresses in the subnet, 

    pings each one, and prints if the host is alive. 

    """ 

    # Create an ip_network object from the given subnet 

    network = ipaddress.ip_network(subnet) 

  

    # Iterate through each IP address in the network (excluding network and broadcast addresses) 

    for ip in network.hosts(): 

        ip = str(ip)  # Convert the IP address object to a string 

        if ping_host(ip):  # Check if the host at this IP is reachable 

            print(f"{ip} is alive")  # Print a message indicating the host is reachable 

  

if __name__ == "__main__": 

    subnet = "10.0.2.0/24"  # Define the subnet to scan (adjust as per your network setup) 

    print("Scanning network...") 

    scan_network(subnet)  # Call the scan_network function with the defined subnet 

    print("Scan complete.")  # Print a message indicating the scan is complete 
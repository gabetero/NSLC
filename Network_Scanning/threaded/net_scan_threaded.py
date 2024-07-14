import ipaddress  # Import the ipaddress module for working with IP addresses and networks
import subprocess  # Import the subprocess module to run external commands
import threading  # Import the threading module to run tasks in parallel

def ping_host(ip):
    """
    Function to ping a host (IP address) to check if it is reachable.

    Parameters:
    - ip: The IP address (as a string) to ping.

    Returns:
    - True if the host is reachable (ping successful), False otherwise.
    """
    # Run the 'ping' command with options to send 1 packet ('-c 1') and wait for 1 second ('-W 1')
    result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Check if the 'ping' command was successful (return code 0 means success)
    if result.returncode == 0:
        return True  # Host is reachable
    return False  # Host is not reachable

def scan_ip(ip):
    """
    Function to check if a specific IP address is alive.

    Parameters:
    - ip: The IP address (as a string) to check.
    """
    if ping_host(ip):  # Use the ping_host function to check if the IP is reachable
        print(f"{ip} is alive")  # Print a message if the host is reachable

def scan_network(subnet):
    """
    Function to scan a network subnet for active hosts.

    Parameters:
    - subnet: The network subnet (in CIDR notation) to scan, e.g., "192.168.1.0/24".

    This function creates threads to ping each IP address in the subnet in parallel.
    """
    # Create an ip_network object from the given subnet
    network = ipaddress.ip_network(subnet)
    threads = []  # List to keep track of threads

    # Iterate through each IP address in the network (excluding network and broadcast addresses)
    for ip in network.hosts():
        ip = str(ip)  # Convert the IP address object to a string
        # Create a new thread to run the scan_ip function for each IP address
        thread = threading.Thread(target=scan_ip, args=(ip,))
        threads.append(thread)  # Add the thread to the list
        thread.start()  # Start the thread

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    subnet = "10.191.0.0/17"  # Define the subnet to scan (adjust as per your network setup)
    print("Scanning network...")  # Print a message indicating the start of the network scan
    scan_network(subnet)  # Call the scan_network function with the defined subnet
    print("Scan complete.")  # Print a message indicating the scan is complete

import subprocess
import re

# Define a function to query the Team Cymru IP-to-AS mapping service for an IP address
def query_ip_to_as(ip_address):
    try:
        # Execute the whois command to query the IP address
        command = f"whois -h whois.cymru.com ' -v {ip_address}'"
        result = subprocess.check_output(command, shell=True, text=True)
        return result
    except subprocess.CalledProcessError as e:
        # Handle any errors or exceptions here
        return f"Error: {e.output}"

# Sample traceroute data
traceroute_data = """
Timestamp: 2023-11-07 21:24:55, Measurement: 1
traceroute: Warning: www.google.com has multiple addresses; using 172.253.122.105
traceroute to www.google.com (172.253.122.105), 64 hops max, 52 byte packets
 1  ncq1338 (192.168.0.1)  3.760 ms  3.551 ms  3.418 ms
 2  10.181.240.130 (10.181.240.130)  31.161 ms  52.814 ms  35.220 ms
 3  10.181.240.130 (10.181.240.130)  44.671 ms  33.011 ms  19.942 ms
"""

# Define regular expression to match IP addresses in traceroute data
ip_pattern = r"\d+\s+([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)"

# Find and store IP addresses from traceroute data
ip_addresses = re.findall(ip_pattern, traceroute_data)

# Initialize variables to store translated AS paths
as_paths = []

# Query the Team Cymru IP-to-AS mapping service for each IP address
for ip in ip_addresses:
    result = query_ip_to_as(ip)
    as_paths.append(result)

# Print the translated AS paths
for as_path in as_paths:
    print(as_path)

import subprocess
import requests

# Function to collect traceroute data
def collect_traceroute_data(destination):
    try:
        # Execute the traceroute command for the destination
        command = ["traceroute", destination]
        result = subprocess.check_output(command, text=True, stderr=subprocess.STDOUT)
        return result
    except subprocess.CalledProcessError as e:
        # Handle any errors or exceptions here
        return f"Error: {e.output}"

# Function to translate router IP addresses to AS numbers
def translate_to_as_numbers(ip_address):
    response = requests.get(f'https://whois.cymru.com/cgi-bin/whois.cgi?detailed=AS&as=AS{ip_address}')
    if response.status_code == 200:
        data = response.text.split('|')
        if len(data) >= 1:
            return data[0].strip()
    return None

# Example usage:
destination = "www.google.com"
traceroute_data = collect_traceroute_data(destination)

# Process the traceroute data to extract router IP addresses and translate to AS numbers
router_ips = extract_router_ips(traceroute_data)
as_numbers = [translate_to_as_numbers(ip) for ip in router_ips]

# Now, you can save the data into a spreadsheet and proceed with analysis.

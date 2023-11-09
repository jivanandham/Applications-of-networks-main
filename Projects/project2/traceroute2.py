import subprocess

def get_as_number(ip_address):
    try:
        # Run the 'whois' command and capture the output
        cmd = f'whois -h whois.cymru.com " -v {ip_address}"'
        output = subprocess.check_output(cmd, shell=True, text=True)

        # Print the entire output
        print(output)

        # Split the output by '|' and extract the AS number
        lines = output.split('\n')
        if len(lines) > 1:
            data = lines[1].strip().split('|')
            if len(data) >= 1:
                return data[0].strip()
        return None
    except subprocess.CalledProcessError as e:
        # Handle any errors or exceptions here
        return f"Error: {e.output}"

# Example usage
ip_address = "69.83.95.137"
as_number = get_as_number(ip_address)
if as_number:
    print(f"AS number for IP {ip_address}: AS={as_number}")
else:
    print(f"AS number for IP {ip_address} not found.")

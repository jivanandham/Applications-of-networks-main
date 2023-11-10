import subprocess
import time
import requests

# Define the desired source IPv6 address
desired_source_ip = "2600:1016:a010:9cc9:65fe:a9bc:d2cb:ded1"  # Replace with the IPv6 address you want to match

# List of destination domains or IP addresses
destinations = [
    "www.google.com",
    "www.apple.com",
    "www.amazon.com",
    "www.bbc.co.uk",
    "www.nytimes.com",
]

# Number of measurements per hour
x = 10  # Adjust as needed

# Number of hours to collect data (1 day = 24 hours)
y = 24  # Adjust as needed

# Function to collect traceroute data for a destination
def collect_traceroute_data(destination):
    try:
        # Execute the traceroute command for the destination
        command = ["tracert", "-6", destination]  # Use -6 for IPv6 traceroute
        result = subprocess.check_output(command, text=True, stderr=subprocess.STDOUT)
        return result
    except subprocess.CalledProcessError as e:
        # Handle any errors or exceptions here
        return f"Error: {e.output}"

# Function to get the public IPv6 address
def get_public_ipv6():
    response = requests.get('https://api6.ipify.org?format=json')  # Use an IPv6 API
    if response.status_code == 200:
        return response.json()['ip']
    else:
        return None

# Collect and save traceroute data for each destination
for hour in range(1, y + 1):
    print(f"Hour {hour} - Current IPv6: {get_public_ipv6()}")

    # Check if the public IPv6 matches the desired source IPv6
    if get_public_ipv6() == desired_source_ip:
        for measurement in range(1, x + 1):
            for destination in destinations:
                print(f"Measurement {measurement} - Traceroute data for {destination}:")

                traceroute_data = collect_traceroute_data(destination)
                print(traceroute_data)

                # Save traceroute data to a text file
                filename = f"hour_{hour}_{destination.replace('.', '_')}_measurement_{measurement}_traceroute.txt"
                with open(filename, 'w') as file:
                    file.write(traceroute_data)

                print(f"Traceroute data saved to {filename}\n")
            time.sleep(3600)  # Wait for 1 hour before the next measurement

    else:
        print("Skipping data collection due to mismatching source IPv6.")

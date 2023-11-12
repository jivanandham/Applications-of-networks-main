import subprocess
import time
import requests
from datetime import datetime

# Define the desired source IPv6 address
desired_source_ipv6 = "2600:1016:a010:cc8a:e045:e603:68d5:60bb"  # Replace with the IPv6 address you want to match

# List of destination domains or IPv4 addresses
destinations = [
    "www.google.com",
    "www.nytimes.com",
    "www.microsoft.com",
    "www.ibm.com",
    "www.github.com",
]

# Number of measurements per hour
x = 10  # Adjust as needed

# Number of hours to collect data (1 day = 24 hours)
y = 24  # Adjust as needed

# Function to collect traceroute data for a destination (IPv4)
def collect_traceroute_data_ipv4(destination):
    try:
        # Execute the traceroute command for the destination
        command = ["tracert", destination]
        result = subprocess.check_output(command, text=True, stderr=subprocess.STDOUT)

        # Create a timestamp with the current date and time
        timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

        return result, timestamp
    except subprocess.CalledProcessError as e:
        # Handle any errors or exceptions here
        return f"Error: {e.output}", timestamp

# Function to get the public IPv6 address
def get_public_ipv6():
    response = requests.get('https://api64.ipify.org?format=json')
    if response.status_code == 200:
        return response.json()['ip']
    else:
        return None

# Collect and save traceroute data for each IPv4 destination
for hour in range(1, y + 1):

    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    print(f"Hour {hour} - Current IPv6: {get_public_ipv6()}")

    # Check if the public IPv6 matches the desired source IPv6
    if get_public_ipv6() == desired_source_ipv6:
        for measurement in range(1, x + 1):
            for destination in destinations:
                print(f"Measurement {measurement} - Traceroute data for {destination}:")

                traceroute_data, timestamp = collect_traceroute_data_ipv4(destination)
                print(traceroute_data)

                # Save traceroute data to a text file with date and time
                filename = f"hour_{timestamp}_{destination.replace('.', '_')}_measurement_{measurement}_traceroute.txt"
                with open(filename, 'w') as file:
                    file.write(traceroute_data)

                print(f"Traceroute data saved to {filename}\n")
            time.sleep(3600)  # Wait for 1 hour before the next measurement

    else:
        print("Skipping data collection due to mismatching source IPv6.")

import subprocess
import time
import requests
from datetime import datetime
import csv

# Define the list of desired source IPv6 addresses
desired_source_ipv6_addresses = [
    "2600:1016:a010:8ac3:c0bb:e2c8:f703:771b",
    # Add more IPv6 addresses as needed
]

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
def collect_traceroute_data_ipv4(destination, hour, measurement):
    try:
        # Execute the traceroute command for the destination
        command = ["traceroute", destination]
        result = subprocess.check_output(command, text=True, stderr=subprocess.STDOUT)

        # Create a timestamp with the current date and time
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create a string with the timestamp and measurement number
        header = f"Timestamp: {timestamp}, Measurement: {measurement}\n"
        return header + result
    except subprocess.CalledProcessError as e:
        # Handle any errors or exceptions here
        return f"Error: {e.output}"

# Function to get the public IPv6 address
def get_public_ipv6():
    response = requests.get('https://api64.ipify.org?format=json')
    if response.status_code == 200:
        return response.json()['ip']
    else:
        return None

# Initialize a CSV file to save the traceroute data
csv_filename = "traceroute_data.csv"
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Source_IPv6", "Destination", "Timestamp", "Measurement", "Traceroute_Data"])

    # Collect and save traceroute data for each IPv6 source and destination
    for source_ipv6 in desired_source_ipv6_addresses:
        for hour in range(1, y + 1):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Check if the public IPv6 matches the desired source IPv6
            if get_public_ipv6() == source_ipv6:
                for measurement in range(1, x + 1):
                    for destination in destinations:
                        print(f"Measurement {measurement} - Traceroute data for {destination}:")
                        print(f"Hour {hour} - Current IPv6: {get_public_ipv6()}")

                        traceroute_data = collect_traceroute_data_ipv4(destination, hour, measurement)
                        print(traceroute_data)

                        # Save traceroute data to the CSV file
                        csv_writer.writerow([source_ipv6, destination, timestamp, measurement, traceroute_data])

                        print(f"Traceroute data saved to CSV\n")
                    time.sleep(3600)  # Wait for 1 hour before the next measurement
            else:
                print("Skipping data collection due to mismatching source IPv6.")

print(f"Data collection completed. Traceroute data saved to {csv_filename}")

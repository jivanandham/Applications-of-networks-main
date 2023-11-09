import re

# Sample traceroute data
traceroute_data = """
Timestamp: 2023-11-07 21:24:55, Measurement: 1
traceroute: Warning: www.google.com has multiple addresses; using 172.253.122.105
traceroute to www.google.com (172.253.122.105), 64 hops max, 52 byte packets
 1  ncq1338 (192.168.0.1)  3.760 ms  3.551 ms  3.418 ms
 2  10.181.240.130 (10.181.240.130)  31.161 ms  52.814 ms  35.220 ms
 3  10.181.240.130 (10.181.240.130)  44.671 ms  33.011 ms  19.942 ms
 4  10.181.240.129 (10.181.240.129)  26.664 ms  15.421 ms
    10.181.240.137 (10.181.240.137)  26.964 ms
 5  137.sub-69-83-95.myvzw.com (69.83.95.137)  35.025 ms  33.804 ms  28.970 ms
 6  141.sub-69-83-95.myvzw.com (69.83.95.141)  16.306 ms  27.023 ms  20.534 ms
 7  * 129.sub-69-83-95.myvzw.com (69.83.95.129)  22.982 ms  31.399 ms
 8  * * *
 9  196.sub-69-83-66.myvzw.com (69.83.66.196)  56.478 ms  29.977 ms  30.321 ms
10  154.sub-69-83-66.myvzw.com (69.83.66.154)  17.093 ms  19.872 ms  19.635 ms
11  155.sub-69-83-66.myvzw.com (69.83.66.155)  22.109 ms  23.256 ms  25.754 ms
12  * * *
13  google-com.customer.alter.net (204.148.170.134)  25.041 ms  34.531 ms  31.383 ms
14  * * *
15  108.170.246.33 (108.170.246.33)  32.611 ms  24.542 ms  24.661 ms
16  108.170.240.98 (108.170.240.98)  30.305 ms
    108.170.246.3 (108.170.246.3)  21.954 ms
    108.170.246.2 (108.170.246.2)  89.800 ms
17  * 216.239.48.95 (216.239.48.95)  51.399 ms
    142.251.49.162 (142.251.49.162)  22.279 ms
18  * 142.250.215.191 (142.250.215.191)  45.921 ms *
19  172.253.79.82 (172.253.79.82)  36.084 ms
    172.253.66.58 (172.253.66.58)  44.691 ms
    172.253.72.204 (172.253.72.204)  36.314 ms
20  172.253.66.147 (172.253.66.147)  30.958 ms
    172.253.66.199 (172.253.66.199)  32.156 ms
    108.170.230.5 (108.170.230.5)  27.810 ms
21  * * *
22  * * *
23  * * *
24  * * *
25  * * *
26  * * *
27  * * *
28  * * *
29  * * *
30  bh-in-f105.1e100.net (172.253.122.105)  31.735 ms  23.721 ms *
"""

# Define regular expressions for extracting data
timestamp_pattern = r"Timestamp: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}), Measurement: (\d+)"
destination_pattern = r"traceroute to (\S+),"
hop_pattern = r"(\d+)  (.+?)  (\d+\.\d+ ms)  (\d+\.\d+ ms)  (\d+\.\d+ ms)"

# Initialize variables to store extracted data
timestamp = ""
measurement = ""
destination = ""
hops = []

# Find timestamp and measurement
timestamp_match = re.search(timestamp_pattern, traceroute_data)
if timestamp_match:
    timestamp = timestamp_match.group

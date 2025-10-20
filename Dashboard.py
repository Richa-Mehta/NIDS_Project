import matplotlib.pyplot as plt
from collections import Counter

# Read the alerts file
with open("alerts.txt", "r") as f:
    lines = f.readlines()

protocols = []
src_ips = []
alerts = 0

for line in lines:
    # Count alerts
    if "ALERT" in line:
        alerts += 1

    # Extract protocol
    if "Protocol:" in line:
        parts = line.split()
        for i, part in enumerate(parts):
            if part == "Protocol:" and i + 1 < len(parts):
                protocols.append(parts[i + 1])

    # Extract Source IP
    if "Source:" in line:
        parts = line.split()
        for i, part in enumerate(parts):
            if part == "Source:" and i + 1 < len(parts):
                src_ips.append(parts[i + 1])

# Count frequency
protocol_count = Counter(protocols)
ip_count = Counter(src_ips)

# Plot protocol distribution
plt.figure(figsize=(10, 5))
plt.bar(protocol_count.keys(), protocol_count.values(), color='purple')
plt.title("Packets per Protocol")
plt.xlabel("Protocol")
plt.ylabel("Count")
plt.show()

# Plot top 5 source IPs
plt.figure(figsize=(10, 5))
plt.bar(list(ip_count.keys())[:5], list(ip_count.values())[:5], color='orange')
plt.title("Top 5 Source IPs")
plt.xlabel("Source IP")
plt.ylabel("Packets Sent")
plt.show()

# Alerts summary
plt.figure(figsize=(5, 5))
plt.pie([alerts, len(lines)-alerts], labels=["Alerts", "Normal"], autopct='%1.1f%%', colors=['red', 'green'])
plt.title("Alert vs Normal Traffic")
plt.show()

from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime
from collections import defaultdict

log_file = "packet_logs.txt"
alert_file = "alerts.txt"

# Dictionary to track packet counts per source IP
packet_count = defaultdict(int)
THRESHOLD = 20  # set your alert threshold

def log_event(file_path, message):
    with open(file_path, "a") as f:
        f.write(message + "\n")

def packet_callback(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst

        # Detect HTTP, DNS, ICMP packets only
        if packet.haslayer(TCP) and packet[TCP].dport == 80:
            proto_name = "HTTP"
        elif packet.haslayer(UDP) and packet[UDP].dport == 53:
            proto_name = "DNS"
        elif packet.haslayer(ICMP):
            proto_name = "ICMP"
        else:
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {proto_name}: {src} -> {dst}"

        # Write normal log
        log_event(log_file, log_entry)
        print(log_entry)

        # Count packets from each source IP
        packet_count[src] += 1

        # If one IP crosses threshold, alert
        if packet_count[src] > THRESHOLD:
            alert_msg = f"⚠️ ALERT [{timestamp}]: Suspicious activity detected from {src} ({packet_count[src]} packets)"
            print(alert_msg)
            log_event(alert_file, alert_msg)
            packet_count[src] = 0  # reset after alert

print("🚨 NIDS is now running with anomaly detection... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=False)

# NIDS_Project
# 🛡 Network Intrusion Detection System (NIDS) using Python  

### 🔍 Overview  
This project is a *Network Intrusion Detection System (NIDS)* built using *Python and Scapy*, designed to monitor real-time network traffic, detect suspicious packet patterns, and alert the user via email when potential anomalies are identified.  

It simulates a lightweight intrusion detection tool — capturing, filtering, analyzing, and alerting in a fully automated pipeline.  

---

## 🚀 Features  
- 🧠 *Live Packet Capture* using Scapy  
- ⚙ *Custom Rule-based Anomaly Detection* (packet frequency threshold)  
- 📝 *Alert Logging* into alerts.txt  
- 📧 *Email Notifications* for detected anomalies  
- 🔍 *Integration with Wireshark* for packet visualization  
- 💻 Works smoothly on *Ubuntu (VirtualBox / Native)*  

---

## 🧠 Learning Outcomes  
- Real-time *packet sniffing* & protocol analysis  
- Understanding *Ethernet, IP, TCP/UDP* layers  
- *Anomaly detection* through packet frequency analysis  
- Email alert automation using *SMTP*  
- Hands-on with *Wireshark, **Python Scapy*, and Linux environments  

---

## ⚙ Tech Stack  
| Component | Technology Used |
|------------|-----------------|
| Language | Python 3.12 |
| Libraries | Scapy, smtplib, email, datetime |
| Platform | Ubuntu (VirtualBox) |
| Tools | Wireshark, VS Code |
| Output | Email alerts + Log file |

---

## 🧩 Workflow  
1. *Capture Packets* → using Scapy’s sniff() function  
2. *Filter & Analyze* → detect repetitive or abnormal packets  
3. *Log Events* → suspicious traffic recorded in alerts.txt  
4. *Trigger Alerts* → email notification with anomaly info  
5. *Visualize Data* → view packets in Wireshark  

---

## 📬 Email Alert Example  
When a suspicious pattern (like repetitive UDP packets) is detected, an email is automatically sent with:  
- Timestamp  
- Type of anomaly  
- Source & Destination IPs  
- Log reference for review  

---

## 🧑‍💻 Team  
| Name | Role | GitHub |
|------|------|--------|
| *Richaa* | Project Lead, Core Developer | [github.com/Richa-Mehta](https://github.com/Richa-Mehta) |
| *Tanmay* | Co-Developer, Testing & Debugging | [github.com/tanmay10628](https://github.com/tanmay10628) |



---

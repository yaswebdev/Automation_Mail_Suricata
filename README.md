# 📧 Suricata Alert Email Notifier

A Python script that monitors Suricata's `eve.json` log file for specific alerts (e.g., ICMP, AnyDesk, TeamViewer) and sends email notifications when such alerts are detected.

---

## 🔒 Use Case

This tool is ideal for cybersecurity professionals or system administrators who want real-time alerting on specific Suricata IDS events. You can use it in a small enterprise, home lab, or educational project for detecting suspicious traffic or tools used by attackers.

---

## 🚀 Features

- ✅ Real-time monitoring of Suricata alerts
- ✅ Alerts based on custom keyword matching (e.g., `icmp`, `anydesk`, `teamviewer`)
- ✅ Sends detailed alert emails via SMTP
- ✅ Prevents duplicate alert notifications
- ✅ Easily configurable

---

## 🛠️ Requirements

- Python 3.x
- Suricata (properly configured to log alerts in `eve.json`)
- Access to a valid SMTP email account (e.g., Gmail)

---

## 📦 Installation

1. Clone the repository or copy the script:

```bash
git clone https://github.com/yourusername/suricata-email-notifier.git
cd suricata-email-notifier


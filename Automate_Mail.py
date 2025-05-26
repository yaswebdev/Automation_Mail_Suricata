import time
import json
import smtplib
from email.mime.text import MIMEText

# Configuration
SURICATA_ALERT_FILE = "/var/log/suricata/eve.json"
SENDER_EMAIL = "your_email@gmail.com"
RECEIVER_EMAIL = "receiver_email@example.com"
EMAIL_PASSWORD = "your_app_password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Track already sent alert messages
sent_alerts = set()

# Keywords to detect in alert (protocol or signature)
KEYWORDS = ["icmp", "anydesk", "teamviewer"]

def send_email(alert_message):
    msg = MIMEText(alert_message)
    msg["Subject"] = "🚨 Suricata Alert Detected"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, EMAIL_PASSWORD)
            server.send_message(msg)
        print("✅ Alert sent:", alert_message.strip())
    except Exception as e:
        print("❌ Failed to send alert:", e)

def monitor_suricata_alerts():
    print("🔍 Monitoring Suricata alerts for ICMP, AnyDesk, and TeamViewer...")

    with open(SURICATA_ALERT_FILE, "r") as file:
        file.seek(0, 2)  # Move to end of file

        while True:
            line = file.readline()
            if not line:
                time.sleep(1)
                continue

            try:
                data = json.loads(line)

                if data.get("event_type") == "alert":
                    protocol = data.get("proto", "").lower()
                    signature = data["alert"]["signature"].lower()

                    if any(k in protocol or k in signature for k in KEYWORDS):
                        src_ip = data.get("src_ip", "unknown")
                        dest_ip = data.get("dest_ip", "unknown")
                        alert_msg = f"{data['alert']['signature']} - {src_ip} -> {dest_ip}"

                        if alert_msg not in sent_alerts:
                            sent_alerts.add(alert_msg)
                            send_email(alert_msg)

            except json.JSONDecodeError:
                continue  # Skip malformed lines

if __name__ == "__main__":
    monitor_suricata_alerts()


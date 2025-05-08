
import os
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Simulated GPT-like summary
summary = f"""CREM.OS Summary – {datetime.now().strftime('%B %d, %Y')}

📍 150 units scanned  
📆 3 leases expiring this month  
🔧 4 maintenance issues flagged  
🚪 2 units vacant for more than 7 days  
AI recommends reviewing lease renewals on Units 108, 134, and 201
"""

# Email setup
EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")
TO_EMAIL = EMAIL_USER  TO_EMAIL = "billionopoly@gmail.com"


msg = MIMEText(summary)
msg["Subject"] = "📬 CREM.OS Portfolio Summary"
msg["From"] = EMAIL_USER
msg["To"] = TO_EMAIL

try:
    print("📤 Connecting to Gmail SMTP...")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, TO_EMAIL, msg.as_string())
    print("✅ Summary email sent successfully.")
except Exception as e:
    print("❌ Failed to send email:", e)

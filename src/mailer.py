import smtplib
from email.mime.text import MIMEText

def send_email(to_address: str, subject: str, body: str) -> str:
    from_address = "your@gmail.com"
    password = "your_app_password"  # use app password if Gmail

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_address
    msg["To"] = to_address

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_address, password)
            server.sendmail(from_address, to_address, msg.as_string())
        return "Email sent successfully."
    except Exception as e:
        return f"Failed to send email: {str(e)}"
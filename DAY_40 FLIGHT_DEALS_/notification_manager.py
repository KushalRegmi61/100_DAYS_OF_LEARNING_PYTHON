from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

# Load environment variables from .env file
load_dotenv()

class NotificationManager:
    def __init__(self):
        self.my_email = os.getenv("MY_EMAIL")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        if not self.my_email or not self.email_password:
            raise ValueError("Email or password environment variables are not set.")

    def send_email(self, fname, lname, email, message):
        try:
            # Create the MIMEText message
            msg = MIMEText(f"Dear {fname} {lname},\n{message}", 'plain', 'utf-8')
            msg['Subject'] = "LOW PRICE ALERT!"
            msg['From'] = self.my_email
            msg['To'] = email

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.email_password)
                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=email,
                    msg=msg.as_string()
                )
            print(f"Email sent successfully to {email}")
        except Exception as e:
            print(f"Failed to send email: {e}")

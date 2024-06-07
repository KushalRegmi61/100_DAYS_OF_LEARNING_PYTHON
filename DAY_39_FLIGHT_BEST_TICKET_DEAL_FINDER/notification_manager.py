from twilio.rest import Client
class NotificationManager:
    def __init__(self, ssid, auth_token):
        self.account_sid=ssid
        self.auth_token=auth_token
        if not self.account_sid or not self.auth_token:
            raise ValueError("Twilio account SID and auth token must be set in environment variables.")
        
        self.client = Client(self.account_sid, self.auth_token)

    def send_whatsapp_message(self, recipient, message):
        try:
            message = self.client.messages.create(
                from_='whatsapp:+14155238886',
                body=message,
                to=f'whatsapp:{recipient}'
            )
            print(f"WhatsApp message sent to {recipient}: {message.sid}")
        
        except Exception as e:
            print(f"Error Occurred: {e}")


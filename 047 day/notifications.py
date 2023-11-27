import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ.get("TW_A_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TW_TOKEN")


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_whatsapp_message(self, user, message):
        message = self.client.messages.create(
            body=message,
            from_="whatsapp:+14155238886",
            to="whatsapp:" + user["whatsApp"]
        )
        return message.status

    @staticmethod
    def format_message(flight):
        return f"Low price alert! {flight['price']}€ to fly from {flight['cityFrom']}-{flight['flyFrom']} " \
               f"to {flight['cityTo']}-{flight['flyTo']}, from {flight['local_departure'].split('T')[0]} " \
               f"to {flight['local_arrival'].split('T')[0]}."

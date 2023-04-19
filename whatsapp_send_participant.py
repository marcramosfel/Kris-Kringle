# First, you need to install the twilio library via pip
# Run the following command in your terminal:
# pip install twilio
import os
from twilio.rest import Client


# AUTH TOKEN LIVE
# 59dbdf2819cb536a3711ecd1a4f350ea


def send_whatsapp_message(phone_number, message):
    # Twilio account details
    account_sid = 'AC46e411b3da63388abb81a31347417510'
    auth_token = os.environ.get('TWILIO_API_KEY')
    client = Client(account_sid, auth_token)

    # Use the Twilio API to send a WhatsApp message
    message = client.messages.create(
        from_='whatsapp:+14155238886',  # Twilio's WhatsApp Sandbox number
        body=message,
        to=f'whatsapp:{phone_number}'
    )

    print(f'Message sent to {phone_number} with ID {message.sid} via Whatsapp')


def send_sms_message(phone_number, message):
    # Twilio account details
    account_sid = 'AC46e411b3da63388abb81a31347417510'
    auth_token = os.environ.get('TWILIO_API_KEY')
    client = Client(account_sid, auth_token)

    # Use the Twilio API to send a WhatsApp message
    message = client.messages.create(
        from_='+16073604544',  # Twilio's WhatsApp Sandbox number
        body=message,
        to=f'{phone_number}'
    )

    print(f'Message sent to {phone_number} with ID {message.sid} via sms')




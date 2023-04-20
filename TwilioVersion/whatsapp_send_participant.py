# First, you need to install the twilio library via pip
# Run the following command in your terminal:
# pip install twilio
import os
from twilio.rest import Client


class SendMessage:
    account_sid = 'AC46e411b3da63388abb81a31347417510'
    auth_token = os.environ.get('TWILIO_API_KEY')
    client = Client(account_sid, auth_token)
    twilio_whatsapp_number = 'whatsapp:+14155238886'
    twilio_sms_number = '+16073604544'

    def __init__(self, phone_number, message):
        self._phone_number = phone_number
        self._message = message


def send_pdf_via_twilio(phone_number, pdf_file_path):
    # Realiza o upload do arquivo PDF para o servidor do Twilio

    with open(pdf_file_path, 'rb') as f:
        media_url = SendMessage.client.messages \
            .create(
            from_=SendMessage.twilio_whatsapp_number,
            body="Segue o PDF que você solicitou.",
            to=phone_number,
            media_url=[f]
        ).media_list[0].uri

        print(f"PDF enviado com sucesso. URL da mídia: {media_url}")
        print(f'Message sent to {phone_number} with ID {message.sid} via sms')


def send_whatsapp_message(phone_number, message):
    # Use the Twilio API to send a WhatsApp message
    message = SendMessage.client.messages.create(
        from_=SendMessage.twilio_whatsapp_number,  # Twilio's WhatsApp Sandbox number
        body=message,
        to=f'whatsapp:{phone_number}'
    )

    print(f'Message sent to {phone_number} with ID {message.sid} via Whatsapp')


def send_sms_message(phone_number, message):
    # Use the Twilio API to send a WhatsApp message
    message = SendMessage.client.messages.create(
        from_=SendMessage.twilio_sms_number,  # Twilio's WhatsApp Sandbox number
        body=message,
        to=f'{phone_number}'
    )

    print(f'Message sent to {phone_number} with ID {message.sid} via sms')

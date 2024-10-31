from . import twilio_client

def send_sms_alert(description, latitude, longitude, recipient):
    message_body = f"Security Alert: {description} at {latitude}, {longitude}"
    message = twilio_client.messages.create(
        body=message_body,
        from_='+15097923288',
        to=recipient
    )
    return message.sid

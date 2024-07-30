import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email():
    message = Mail(
        from_email=os.getenv('EMAIL_FROM'),
        to_emails=os.getenv('EMAIL_TO'),
        subject=os.getenv('EMAIL_SUBJECT'),
        plain_text_content=os.getenv('EMAIL_BODY')
    )
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    send_email()

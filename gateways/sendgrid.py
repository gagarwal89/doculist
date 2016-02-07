import sendgrid

client = sendgrid.SendGridClient('YOUR_SENDGRID_API_KEY')


class SendgridGateway:
    def send_mail(to_email, subject, body):
        message = sendgrid.Mail(to=to_email, subject=subject, text=body, from_email='gagarwal89@gmail.com')  # noqa
        status, msg = client.send(message)

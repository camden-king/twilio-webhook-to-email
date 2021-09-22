from flask import Flask, request
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from twilio.twiml.messaging_response import MessagingResponse

application = Flask(__name__)

# To setup fill in variables below
NUMBER_TO_EMAIL_MAPPING = {
    "+11234567890" : "example@example.com", # replace with phone numbers of users and the email the texts should be sent to
    "+10987654321" : "test@example.com",
}
SENDGRID_API_KEY = '' # replace with your own key
SENDGRID_FROM_EMAIL = 'example@example.com' # replace with your own email address (verified sender)

@application.route("/sms", methods=['POST'])
def sms_reply():
    """Takes a incoming text message and sends the body to the corresponding email address."""
    From = request.values.get("From", "")
    Message = request.values.get("Body", "")

    if From in NUMBER_TO_EMAIL_MAPPING:
        send_email(NUMBER_TO_EMAIL_MAPPING[From], "Text Message From %s" % From,  Message)

    resp = MessagingResponse()
    return str(resp)

@application.route("/", methods=['GET'])
def hello_world():
    return "Hello, world! Your program is successfully running."


def send_email(to, subject, message):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    from_email = Email(SENDGRID_FROM_EMAIL)  
    to_email = To(to)  
    subject = subject
    content = Content("text/plain", message)
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)


if __name__ == "__main__":
    application.run(debug=True)
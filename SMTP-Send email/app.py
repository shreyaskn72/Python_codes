# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage


# task 1 sending email
def maillsend(sender, receiver, subject, message):

    # host from json if required
    # port from json if required.
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.set_content(message)

    try:
        with smtplib.SMTP('localhost', 25) as s:     # with SMTP(host='smtp.example.org', port=587) as smtp_server:
            #s.login(user='user@smtp.example.org', password='password')   # give the username and password, not required in certain companies
            s.send_message(msg)
            print("Successfully sent email")

    except:
        print("failed to send email")

if __name__ == "__main__":

    sender = "sssssss@email.com"

    receiver = "ccccccc@email.com"

    subject = "trial email"

    message = "Hope you and your family is in sound health"

    maillsend(sender, receiver, subject, message)
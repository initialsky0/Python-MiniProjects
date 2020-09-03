import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

PATH = './send-emails/'

def test_send_email():
    html = Template(Path(f'{PATH}index.html').read_text())

    email = EmailMessage()
    email['from'] = 'user'
    email['to'] = 'somebody@something.com'
    email['subject'] = 'This is the subject'
    
    # This is the body of the email
    email.set_content(html.substitute({'name': 'username'}), 'html')

    # host can be different base on email platform, port typically is 587
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        # hello message
        smtp.ehlo()
        smtp.starttls()
        smtp.login('theemailaddress@gmail.com', 'passwordhere')
        smtp.send_message(email)
    return 0

def main():
    # test_send_email()
    return 0

if __name__ == "__main__":
    main()
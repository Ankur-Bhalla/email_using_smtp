# Customize email using html based Emails with Python Using smtplib, email, string and pathlib modules.
# Create html index.html file and write message which will be dynamically called by python script
# (email_sender_html_based.py) file.


import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())  # convert html file into string
email = EmailMessage()
email['from'] = 'Ankur Bhalla'
email['to'] = '<enter receiver email>'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')  # Dynamic message substituted using index.html file

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # SMTP.ehlo(name=''). Identify yourself to an ESMTP server using EHLO.
    smtp.ehlo()

    # SMTP.starttls(keyfile=None, certfile=None, context=None)
    # Put the SMTP connection in TLS (Transport Layer Security) mode. All SMTP commands that follow
    # will be encrypted. You should then call ehlo() again.
    smtp.starttls()

    # SMTP.login(user, password, *, initial_response_ok=True)
    # Log in on an SMTP server that requires authentication. The arguments are the username and the
    # password to authenticate with.
    smtp.login('<enter sender email>', '<enter sender password>')

    # SMTP.send_message(msg, from_addr=None, to_addrs=None, mail_options=(), rcpt_options=()).
    # This is a convenience method for calling sendmail() with the message represented by an
    # email.message.Message object.
    smtp.send_message(email)

    print('all good boss!')

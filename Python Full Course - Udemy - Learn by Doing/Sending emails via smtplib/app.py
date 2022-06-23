"""
Enable less secure apps
Do not have 2 factor authentication on
"""

import smtplib
from email.message import EmailMessage

email_content = '''Dear Sir / Madam,

I am sending you an email with python'''

email = EmailMessage()

email['Subject'] = 'Test Email'
email['From'] = 'jatins368@gmail.com'
email['to'] = 'jatins368@gmail.com'

email.set_content(email_content)

smtp_connector = smtplib.SMTP(host='smtp.gmail.com', port=587)

smtp_connector.starttls()

smtp_connector.login('jatins368@gmail.com', 'principe@281sangita')

smtp_connector.send_message(email)
smtp_connector.quit()




import smtplib
import time
import imaplib
import email
import os
from pdf_reader import Extract_Pdf
from email.utils import parsedate_to_datetime
from dateutil import tz
from dateutil.tz import tzutc, tzlocal
from datetime import datetime, timezone, timedelta
# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

import os
dirname = os.path.dirname(__file__)
tmppdf = os.path.join(dirname, 'tmp.pdf')

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "dummyemail" + ORG_EMAIL
FROM_PWD    = "password"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def read_email_from_gmail(start_time):
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        emails=[]

        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(str(i), '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    if parsedate_to_datetime(msg.get('date')).replace(tzinfo=tzlocal()).astimezone(tzutc()) < start_time - timedelta(minutes=1):
                        continue
                    emails.append("")
                    email_subject = msg['subject']
                    email_from = msg['from']
                    if email_from:
                        emails[len(emails)-1]+='From : ' + email_from + '\n'
                    if email_subject:
                        emails[len(emails)-1]+='Subject : ' + email_subject + '\n'
                    for part in msg.walk():
                        if part.get_content_maintype() == 'multipart':
                            continue
                        if part.get('Content-Disposition') is None:
                            continue
                        if part.get_filename()==None:
                            continue
                        print(part.get_filename())
                        if os.path.splitext(part.get_filename())[1].find(".pdf")!=-1:
                            fp = open(tmppdf, 'wb')
                            fp.write(part.get_payload(decode=True))
                            fp.close()
                            emails[len(emails)-1]+=Extract_Pdf(tmppdf) + '\n'

        return emails

    except Exception as e:
        print(str(e))
        return "couldnt access inbox"

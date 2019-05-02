The libraries needed for this module to work are found in requirements.txt, along with the required version.
Install the libraries first.

To poll the email address, set the variables FROM_EMAIL and FROM_PWD in email_poller.py to the corresponding address and password.

To set the desired webhook url, set the variable webhook_url in data_pusher.py.

Every time main.py is run, it will retrieve timestamp of previous run 
and poll all emails received in inbox after the timestamp value, parse all the pdf attachments, 
post the text data of pdfs along with email sender and email subject to webhook url, then update run timestamp.

It is advised to create a cron job that would run main.py script at a regular interval,
in order for the polling to be automated.

If you are using a gmail address for the polling, you might need to turn on the setting: Allow less secure apps

Best Regards.

 
import os
import glob
import time
import smtplib
from email.mime.text import MIMEText

time_gap = 5
targets = []  # Insert a list of target folders.

alert_server = "Insert mail server address."
alert_server_port = "Insert server port as Int."
alert_recipient = "Insert recipient e-mail address."
alert_sender = "Insert sender e-mail."
alert_sender_user = os.environ['ALERT_SENDER_USER']
alert_sender_pswd = os.environ['ALERT_SENDER_PSWD']
alert_subject = "Insert alert subject."
alert_body = "Insert message body."


def get_latest(target):
    files = glob.glob(target)
    latest_file = max(files, key=os.path.getctime)
    return latest_file


def get_size(file):
    return os.path.getsize(file)


def get_diff(target):
    size_initial = get_size(target)
    time.sleep(time_gap)
    size_final = get_size(target)

    return size_final - size_initial


def send_alert(target):
    
    server = smtplib.SMTP_SSL(alert_server, alert_server_port)
    server.login(alert_sender_user, alert_sender_pswd)

    message = MIMEText(msg_body, 'html')
    message['From'] = alert_sender
    message['To'] = alert_recipient
    message['Subject'] = alert_subject

    server.send_message(message)


def main():

    for target in targets:
        file = get_latest(target)
        diff = get_diff(file)

        if diff == 0:
            send_alert(target)


if __name__ == "__main__":
    main()

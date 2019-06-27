import os
import glob
import time
import smtplib
from email.mime.text import MIMEText

time_gap = 5
source = "target_list.txt"
targets = []

alert_server = os.environ['ALERT_SERVER']
alert_server_port = os.environ['ALERT_SERVER_PORT']
alert_recipient = os.environ['ALERT_RECIPIENT']
alert_sender = os.environ['ALERT_SENDER']
alert_sender_user = os.environ['ALERT_SENDER_USER']
alert_sender_pswd = os.environ['ALERT_SENDER_PSWD']


def list_targets(source):
    with open(source) as f:
        return f.read().splitlines()


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

    body =  "Insert message here."

    message = MIMEText(body, 'html')
    message['From'] = alert_sender
    message['To'] = alert_recipient
    message['Subject'] = "Recording Alert"

    server.send_message(message)


def main():

    targets = list_targets(source)

    for target in targets:
        file = get_latest(target)
        diff = get_diff(file)

        if diff == 0:
            send_alert(target)


if __name__ == "__main__":
    main()

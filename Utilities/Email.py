import smtplib
from email.message import EmailMessage
import os
import configparser

def send_email_with_report(report_path, config_path='Configurations/config.ini'):
    """
    Sends an email with the given report attached.
    Email settings are read from the provided config file.
    """
    config = configparser.ConfigParser()
    config.read(config_path)
    receiver_email = config['EMAIL']['receiver']
    sender_email = config['EMAIL']['sender']
    sender_password = config['EMAIL']['password']

    msg = EmailMessage()
    msg['Subject'] = '🧪 Automation Report'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content('Attached is the latest test automation report.')

    if os.path.exists(report_path):
        with open(report_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(report_path)
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    else:
        raise FileNotFoundError(f"Report not found at: {report_path}")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print("✅ Email sent successfully.")

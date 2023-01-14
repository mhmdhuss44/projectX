import paths
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import yaml

class MailServer:

    def __init__(self):
        self.CONFIGS = None

    def load_mail_server(self):
        conf_yaml=paths.yaml_path
        if conf_yaml.exists():
            with open(file=conf_yaml, mode="r") as yaml_file:
                try:
                    self.CONFIGS = yaml.safe_load(stream=yaml_file.read())
                    print("Configuration yaml file loaded successfully.")
                except yaml.YAMLError as ex:
                    print(f"Failed to load Mail Server configuration file")

    def send_email(self,email_from:str,email_to:str,email_subject:str,email_message:str) -> bool:
    
        email_Result = False
        # initialize connection to our email server, we will use Outlook here
        smtp = smtplib.SMTP(self.CONFIGS["EMAIL_SMTP"], port=self.CONFIGS["EMAIL_PORT"])

        smtp.ehlo()  # send the extended hello to our server
        smtp.starttls()  # tell server we want to communicate with TLS encryption

        smtp.login(self.CONFIGS["EMAIL_USER"],self.CONFIGS["EMAIL_PASS"] )  # login to our email server

        # setup the parameters of the message
        msg = MIMEMultipart() 
        message = email_message
        msg["from"]=email_from
        msg["to"]=email_to
        msg["subject"]=email_subject

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
                    
        try:
            smtp.send_message(msg)
            del msg
            email_Result= True
        except Exception as mail_exception:
            print(f"Email was not sent with the following error:[{mail_exception}]")
        return email_Result
import re
import paths
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import yaml


class MailServer:

    __EMAIL_SUBJECT = "Job results found for company - "
    #subject = f"Job results found for company [{selected_company.company_name}]"


    def __init__(self):
        self.CONFIGS = None

    def load_mail_server(self):
        conf_yaml = paths.YAML_PATH
        if conf_yaml.exists():
            with open(file=conf_yaml, mode="r") as yaml_file:
                try:
                    self.CONFIGS = yaml.safe_load(stream=yaml_file.read())
                    print("Configuration yaml file loaded successfully.")
                except yaml.YAMLError as ex:
                    print(f"Failed to load Mail Server configuration file")

    #  it will open the file and read the content using the yaml.safe_load() method
    #    , and store it in the CONFIGS attribute of the class.

    def send_email(self,person,message,company):

        return self.__email_dispatcher(email_to=person.get_email_address(),
                                                email_subject=self.__EMAIL_SUBJECT + company,
                                                email_message=MailServer.strip_text(message))

    # This function is a method of the MailServer class, it sends an email using the Simple Mail
    # Transfer Protocol (SMTP) library in python.
    def __email_dispatcher(self, email_to: str, email_subject: str, email_message: str) -> bool:

        email_Result = False
        # initialize connection to our email server, we will use Outlook here
        # this info is located in the yaml file
        smtp = smtplib.SMTP(self.CONFIGS["EMAIL_SMTP"], port=self.CONFIGS["EMAIL_PORT"])

        # what are those exactly?
        smtp.ehlo()  # send the extended hello to our server
        smtp.starttls()  # tell server we want to communicate with TLS encryption

        smtp.login(self.CONFIGS["EMAIL_USER"], self.CONFIGS["EMAIL_PASS"])  # login to our email server

        # setup the parameters of the message
        msg = MIMEMultipart()
        message = email_message
        msg["from"] = self.CONFIGS["EMAIL_FROM"]
        msg["to"] = email_to
        msg["subject"] = email_subject

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        try:
            smtp.send_message(msg)
            del msg
            email_Result = True
        except Exception as mail_exception:
            print(f"Email was not sent with the following error:[{mail_exception}]")
        return email_Result

    @staticmethod
    def verify_email(email_to:str) -> bool:

        regex_str = r"[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$"
        match = re.match(regex_str, email_to)
        return bool(match)

    @staticmethod
    def strip_text(text:str) -> str:
        characters:str = ['"',"{","}",'[',']']
        for char in characters:
            if char in text:
                text = text.replace(char, '')
        return text
            


#     The first step is to create a connection to the email server using the SMTP class from the smtplib
#     library. The server's address and port are passed to the constructor of the SMTP class,
#     and the connection is established. The server's address and port are obtained from the yaml file.
#
# The second step is to initiate a handshake with the server. The ehlo() method is used to
# send an extended hello command to the server, which starts the handshake process.
#
# The third step is to establish a secure connection with the server. The starttls() method
# is used to tell the server that we want to communicate with it using
# Transport Layer Security (TLS) encryption. This step is optional but highly recommended.
#
# The fourth step is to authenticate with the server. The login() method is used
# to send the login credentials (username and password) to the server.
# These credentials are obtained from the yaml file as well
#
# The fifth step is to create the email message. A MIMEMultipart object is
# created and the various fields of the email message, such as the sender, recipient, subject,
# and message body, are set.
#
# The sixth step is to send the email message. The send_message() method is used
# to send the email message to the server.
#
# The final step is to check if the email was sent successfully and return
# the result. If the email was sent successfully, the function returns True,
# otherwise it returns False and print the exception error.

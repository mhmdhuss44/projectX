from mail_server import MailServer
from personClass import Person


def run():
    email_from = "men_tor_ing_2023@outlook.com"
    # email_to="mhmdhuss44@gmail.com"
    subject = "This is a testing email"
    message = "Hi from my email server2"

    my_mail = MailServer()
    my_mail.load_mail_server()
    send_email_result = my_mail.send_email(email_from=email_from, email_to=mhmd.get_email_address(),
                                           email_subject=subject, email_message=message)

    if send_email_result:
        print(f"Email was sent successfuly to [{mhmd.get_email_address()}]")
    else:
        print("Error while sending email")


if __name__ == "__main__":
    mhmd = Person("mohamed", 21, "0549366894", "mhmdhuss44@gmail.com")
    run()

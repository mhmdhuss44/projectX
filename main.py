from mail_server import MailServer

def run():
    email_from="men_tor_ing_2023@outlook.com"
    email_to="orsan.awawdi@gmail.com"
    subject = "This is a testing email"
    message="Hi from my email server"

    my_mail=MailServer()
    my_mail.load_mail_server()
    send_email_result = my_mail.send_email(email_from=email_from,email_to=email_to,email_subject=subject,email_message=message)

    if send_email_result:
        print(f"Email was sent successfuly to [{email_to}]")
    else:
        print("Error while sending email")

if __name__=="__main__":
    run()




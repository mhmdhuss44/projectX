from job_finder import JobFinder
from mail_server import MailServer
from personClass import Person
from companies import Companies

def run():

    mohammad = Person("Mohammad", 21, "0549366894", "mhmdhuss44@gmail.com")
    orsan = Person("Orsan", 21, "0549366894", "orsan.awawdi@gmail.com")
    job_finder = JobFinder(company_id=Companies.BMC.company_number)
    message = ', '.join(job_finder.search_by_company_id())

    email_from = "men_tor_ing_2023@outlook.com"
    subject = f"Job results found for company [{Companies.BMC.company_name}]"
    

    my_mail = MailServer()
    my_mail.load_mail_server()
    send_email_result = my_mail.send_email(email_from=email_from, email_to=orsan.get_email_address(),
                                            email_subject=subject, email_message=message)
    
    if send_email_result:
        print(f"Email was sent successfully to [{orsan.get_email_address()}]")
    else:
        print("Error while sending email")


if __name__ == "__main__":
    
    run()

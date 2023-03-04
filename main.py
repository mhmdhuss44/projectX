import json
from job_finder import JobFinder
from mail_server import MailServer
from personClass import Person
from companies import Companies
from email_validator import validate_email, EmailNotValidError

def run():
    company = Companies.CHEVRON
    mohammad = Person("Mohammad", 21, "0549366894", "mhmdhuss44@gmail.com")
    orsan = Person("Orsan", 21, "0549366894", "orsan.awawdi@gmailcom")
    job_finder = JobFinder(company_number=company.company_number)

    email_from = "men_tor_ing_2023@outlook.com"
    subject = f"Job results found for company [{company.company_name}]"
    message=json.dumps(job_finder.search_by_company_id(),indent=2)
    
    my_mail = MailServer()
    my_mail.load_mail_server()
    try:
        validate_email(orsan.get_email_address()).email
        send_email_result = my_mail.send_email(email_from=email_from, email_to=orsan.get_email_address(),
                                            email_subject=subject, email_message=MailServer.strip_text(message))
        if send_email_result:
            print(f"Email was sent successfully to [{orsan.get_email_address()}]")
    except EmailNotValidError as e: 
        print(f"Invalid email address:[{orsan.get_email_address()}]")

if __name__ == "__main__":
    
    run()

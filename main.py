import dataclasses
import json
from job_finder import JobFinder
from mail_server import MailServer
from personClass import Person
from companies import Companies
from email_validator import validate_email, EmailNotValidError
import logging

class Main():

    def __init__(self, person:Person, company:Companies=Companies.BMC):

        self.__company = company
        self.__person = person

    def run(self,):
        self.__set_logger()

        job_finder_result = JobFinder(company_number=self.__company.company_number)
        message=json.dumps(job_finder_result.search_by_company_id(),indent=2)
        
        my_mail = MailServer()
        my_mail.load_mail_server()
        try:
            email_Address = self.__person.get_email_address()
            logging.info(f"Validating email [{email_Address}].")
            validate_email(email_Address)

            send_email_result = my_mail.send_email(company=self.__company.company_name,
                                                    person= self.__person,
                                                    message=message)

            if send_email_result:
                logging.info(f"Email was sent successfully to [{self.__person.get_email_address()}].")
        except EmailNotValidError as e: 
            logging.error(f"Invalid email address:[{self.__person.get_email_address()}].")
        except BaseException as ex:
            logging.error(f"Error occured:[{ex}].")

    def __set_logger(self):
        
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            datefmt="%d-%m-%Y %H:%M:%S",)
if __name__ == "__main__":

    chevron = Companies.CHEVRON
    orsan = Person("Orsan", 21, "0549366894", "orsan.awawdi@gmail.com")
    main = Main(company=chevron,person=orsan)
    main.run()

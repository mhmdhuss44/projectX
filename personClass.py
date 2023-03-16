class Person:
    def __init__(self, name:str="Mohammad", age:int=21, phone_number:str="0549366894", email_address:str="mhmdhuss44@gmail.com"):
        # The constructor
        self.__name = name
        self.__age = age
        self.__phone_number = phone_number
        self.__email_address = email_address
        # TODO: make all members private

    def get_name(self):
        # Returns the value of the name
        return self.__name

    def set_name(self, name):
        # change the value of the name
        self.__name = name

    # The following get/set functions do the same for the other attributes
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_email_address(self):
        return self.__email_address

    def set_email_address(self, email_address):
        self.__email_address = email_address


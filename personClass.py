class Person:
    def __init__(self, name, age, phone_number, email_address):
        # The constructor
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.__email_address = email_address
        # TODO: make all members private

    def get_name(self):
        # Returns the value of the name
        return self.name

    def set_name(self, name):
        # change the value of the name
        self.name = name

    # The following get/set functions do the same for the other attributes
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_email_address(self):
        return self.__email_address

    def set_email_address(self, email_address):
        self.__email_address = email_address

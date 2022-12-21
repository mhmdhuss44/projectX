# import the Person class from the personClass
from personClass import Person

person1 = Person('mhmd huss', 21, '0549366894')


print(person1.get_name())
print(person1.get_age())
print(person1.get_phone_number())

person1.set_name("king")
person1.set_age(30)
person1.set_phone_number("884444")

print(person1.get_name())
print(person1.get_age())
print(person1.get_phone_number())


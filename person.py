class Person:
    def __init__(self, name, age, phone, email):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    def display_person(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Phone  : {self.phone}")
        print(f"Email  : {self.email}")

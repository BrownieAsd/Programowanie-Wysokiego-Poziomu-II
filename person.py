class Company:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.say_hello()

    @classmethod
    def say_hello(cls):
        return (f"Hi, my name is{cls.name} and my last name is {cls.last_name} and my age is {cls.age}")
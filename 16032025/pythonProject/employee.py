import person
class Employee(person.Person):
    def __init__(self, position, salary, person):
        self.person = person
        self.position = position
        self.salary = salary
        self.job_details()

    @classmethod
    def job_details(cls):
        return (f"I work as a {cls.position}, and I earn {cls.salary}")


import employee
import person

class Manager(employee.Employee,person.Person):
    employee_name = ""
    def __init__(self, team,person,employee):
        super().__init__(self, person.first_name, person.last_name,person.age)
        self.person = person
        self.employee = employee
        self.team = team
        self.add_to_team(Manager.employee_name)
        self.say_hello()

    @classmethod
    def add_to_team(cls, employee_name, team):
        team.append(employee_name)
        return cls.team

    @classmethod
    def say_hello(cls):
        return (f"Hi, my name is{cls.name} and my last name is {cls.last_name} and my age is {cls.age}. I Manage{len(cls.team)} People!")
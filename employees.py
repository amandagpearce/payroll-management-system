import datetime
import calendar


class Employee:
    id: int = 0
    name: str = ""  # adding typehint

    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    # if no constructor is defined here in derived class
    #  the base class constructor will be used
    def __init__(self, id, name, rate_per_day):
        # the base class will provide the id and name
        super().__init__(id, name)
        self.rate_per_day = rate_per_day

    def calculate_payroll(self):
        today = datetime.datetime.now()
        totalDays = calendar.monthrange(today.year, today.month)[1]
        return self.rate_per_day * totalDays


class PartTimeEmployee(Employee):
    def __init__(self, id, name, total_hours, rate_per_hour):
        super().__init__(id, name)
        self.total_hours = total_hours
        self.rate_per_hour = rate_per_hour

    def calculate_payroll(self):
        return self.total_hours * self.rate_per_hour


class ComissionEmployee(SalaryEmployee):
    def __init__(self, id, name, rate_per_day, comission):
        super().__init__(id, name, rate_per_day)
        self.comission = comission

    def calculate_payroll(self) -> int:  # -> int = Typehint on method return
        salary = super().calculate_payroll()
        return salary + self.comission


# new requirement: add Manager, Developer, Salesperson(commission employee)
# and intern


class Manager(SalaryEmployee):
    def work(self, hours):
        print(
            f"{self.name} Manager is overseeing the project for {hours} hours"
        )


class Developer(SalaryEmployee):
    def work(self, hours):
        print(
            f"""{self.name} Developer is working on the project for {hours}
            hours"""
        )


class Salesperson(ComissionEmployee):
    def work(self, hours):
        print(
            f"""{self.name} Salesperson is handling client calls for {hours}
            hours"""
        )


class Intern(PartTimeEmployee):
    def work(self, hours):
        print(f"{self.name} Intern has completed their tasks in {hours} hours")


class Consultant(Developer, PartTimeEmployee):
    # should not call super here, instead invoke the PartTimeEmployee constructor directly
    # which can be noticed by checking employees.Consultant.__mro__ in the payrollapp file
    def __init__(self, id, name, total_hours, rate_per_hour):
        PartTimeEmployee.__init__(self, id, name, total_hours, rate_per_hour)

    def calculate_payroll(self):
        return PartTimeEmployee.calculate_payroll(self)

from payroll import SalaryPolicy, ComissionPolicy, PartTimePolicy
from employeemanagement import (
    ManagerRole,
    DeveloperRole,
    SalesRole,
    WorkerRole,
)


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Manager(Employee, ManagerRole, SalaryPolicy):
    def __init__(self, id, name, rate_per_day):
        SalaryPolicy.__init__(
            self, rate_per_day
        )  # invoking the SalaryPolicy constructor here explicitly

        super().__init__(
            id, name
        )  # whenever we're using super it goes to the parent class based on
        # the hierarchy of the MRO; since the first class being inherited is
        # Employee, it goes to the constructor of Employee, where
        # the values of ID and name will be set and since there are no more
        # super() calls, the code execution will stop there


class Developer(Employee, DeveloperRole, SalaryPolicy):
    def __init__(self, id, name, rate_per_day):
        SalaryPolicy.__init__(self, rate_per_day)

        super().__init__(id, name)


class Salesperson(Employee, SalesRole, ComissionPolicy):
    def __init__(self, id, name, rate_per_day, comission):
        ComissionPolicy.__init__(self, rate_per_day, comission)

        super().__init__(id, name)


class Worker(Employee, WorkerRole, PartTimePolicy):
    def __init__(self, id, name, total_hours, rate_per_hour):
        PartTimePolicy.__init__(self, total_hours, rate_per_hour)

        super().__init__(id, name)


class Consultant(Employee, DeveloperRole, PartTimePolicy):
    def __init__(self, id, name, total_hours, rate_per_hour):
        PartTimePolicy.__init__(self, total_hours, rate_per_hour)
        super().__init__(id, name)

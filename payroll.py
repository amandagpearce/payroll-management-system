import datetime
import calendar


class PayrollManagementSystem:  # logical/conceptual interface
    def calculate_payroll(self, employees):
        print("Payroll Management System")
        print("-------------------------")

        for employee in employees:
            print(f"Employee:{employee.id}")
            print(f"Name:{employee.name}")
            print(f"Amount:{employee.calculate_payroll()}")
            print("======================================")


class SalaryPolicy:
    def __init__(self, rate_per_day):
        self.rate_per_day = rate_per_day

    def calculate_payroll(self):
        today = datetime.datetime.now()
        totalDays = calendar.monthrange(today.year, today.month)[1]

        return self.rate_per_day * totalDays


class PartTimePolicy:
    def __init__(self, total_hours, rate_per_day):
        self.total_hours = total_hours
        self.rate_per_day = rate_per_day

    def calculate_payroll(self):
        return self.total_hours * self.rate_per_day


class ComissionPolicy(SalaryPolicy):
    def __init__(self, rate_per_day, comission):
        super().__init__(rate_per_day)
        self.comission = comission

    def calculate_payroll(self):
        salary = super().calculate_payroll()
        return salary + self.comission

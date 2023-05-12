class PayrollManagementSystem:  # logical/conceptual interface
    def calculate_payroll(self, employees):
        print("Payroll Management System")
        print("-------------------------")

        for employee in employees:
            print(f"Employee:{employee.id}")
            print(f"Name:{employee.name}")
            print(f"Amount:{employee.calculate_payroll()}")
            print("======================================")

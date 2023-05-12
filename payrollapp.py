import payroll
import employees
import employeemanagement

manager = employees.Manager(101, "Maria", 5000)
developer = employees.Developer(102, "Amanda", 2500)
salesperson = employees.Salesperson(103, "Vanessa", 1000, 1500)
worker = employees.Worker(104, "Vinicius", 10, 250)
consultant = employees.Consultant(105, "Alberto", 30, 50)

employees = [manager, developer, salesperson, worker, consultant]

employeeperformance = employeemanagement.PerformanceManager()
employeeperformance.track(employees, 40)

payroll_system = payroll.PayrollManagementSystem()
payroll_system.calculate_payroll(employees)

# debugging multiple inheritance issue "diamond problem"
# print(employees.Consultant.__mro__)

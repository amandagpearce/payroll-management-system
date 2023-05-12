import payroll
import employees
import employeemanagement

manager = employees.Manager(101, "Manager_Name", 5000)
developer = employees.Developer(102, "Developer_Name", 2500)
salesperson = employees.Salesperson(103, "Salesperson_Name", 1000, 1500)
intern = employees.Intern(104, "Intern_Name", 10, 250)
consultant = employees.Consultant(105, "Consultant_name", 30, 50)

employees = [manager, developer, salesperson, intern, consultant]

employeeperformance = employeemanagement.PerformanceManager()
employeeperformance.track(employees, 40)

payroll_system = payroll.PayrollManagementSystem()
payroll_system.calculate_payroll(employees)

# debugging multiple inheritance issue "diamond problem"
# print(employees.Consultant.__mro__)

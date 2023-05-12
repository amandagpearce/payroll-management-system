import payroll
import employees
import employeemanagement

salary_employee = employees.SalaryEmployee(101, "salary_employee", 1000)

manager = employees.Manager(101, "Manager_Name", 5000)
developer = employees.Developer(102, "Developer_Name", 2500)
salesperson = employees.Salesperson(103, "Salesperson_Name", 1000, 1500)
intern = employees.Intern(104, "Intern_Name", 10, 250)

employees = [manager, developer, salesperson, intern]

employeeperformance = employeemanagement.PerformanceManager()
employeeperformance.track(employees, 40)

payroll_system = payroll.PayrollManagementSystem()
payroll_system.calculate_payroll(employees)

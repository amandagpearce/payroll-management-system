import payroll

salary_employee = payroll.SalaryEmployee(101,
                                         'salary_employee',
                                         1000)

part_time_employee = payroll.PartTimeEmployee(101,
                                              'part_time_employee',
                                              20,
                                              500)

comission_employee = payroll.ComissionEmployee(103,
                                               'comission_employee',
                                               1000,
                                               500)

payroll_system = payroll.PayrollManagementSystem()
payroll_system.calculate_payroll([salary_employee,
                                  part_time_employee,
                                  comission_employee])

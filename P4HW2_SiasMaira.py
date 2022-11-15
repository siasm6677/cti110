# CTI-110
# P3HW2 - Salary Calculator
# Maira Sias
# 11/15/2022
#
# This program will calculate regular pay, overtime pay, and gross pay for multiple employees using user input
# Number of employees is based on user input until "None" is entered
# Add employee names to a list
# Add overtime pay for each emoloyee to a separate list
# Add regular hours pay for each emoloyee to a separate list
# Add gross pay for each emoloyee to a separate list
# Calculate and display number of employees, total overtime pay, total regular pay and total gross paid for all employees

employee_name = input("Enter employee's name or enter \"None\" to terminate: ")
employee_list = []
over_pay_list = []
reg_pay_list = []
gross_pay_list = []

while employee_name != 'None':
    employee_list.append(employee_name)
    print("How many hours did", employee_name, "work?: ", end=' ')    
    hours_worked = float(input())    
    print(f'{"What is"} {employee_name}\'{"s pay rate?: "}', end=' ')
    pay_rate = float(input())
    print()
    print(f'{"Employee name:":18} {employee_name}')
    print()
    print(f'{"Hours Worked":15} {"Pay Rate":15} {"OverTime":15} {"OverTime Pay":15} {"RegHour Pay":15} {"Gross Pay":15}')
    print("-------------------------------------------------------------------------------------------")
    if hours_worked > 40:
        overtime_hrs = hours_worked - 40
    else:
        overtime_hrs = 0
    overtime_rate = pay_rate * 1.5

    if hours_worked > 40:
        overtime_pay = overtime_hrs * overtime_rate
    else:
        overtime_pay = 0
    
    if hours_worked <= 40:
        reg_hr_pay = hours_worked * pay_rate
    else:
        reg_hr_pay = 40 * pay_rate
    gross_pay = overtime_pay + reg_hr_pay
    print(f'{hours_worked:<15} {pay_rate:<15} {overtime_hrs:<15} $ {overtime_pay:<13.2f} $ {reg_hr_pay:<13.2f} $ {gross_pay:<13.2f}')
    over_pay_list.append(overtime_pay)
    reg_pay_list.append(reg_hr_pay)
    gross_pay_list.append(gross_pay)
    print('\n')
    employee_name = input("Enter employee's name or enter \"None\" to terminate: ")
print()
print(f'{"Total number of employees entered:":<42} {len(employee_list)}')
print(f'{"Total amount payed for overtime:":<40} $ {sum(over_pay_list):.2f}')
print(f'{"Total amount payed for regular hours:":<40} $ {sum(reg_pay_list):.2f}')
print(f'{"Total amount payed in gross:":<40} $ {sum(gross_pay_list):.2f}')

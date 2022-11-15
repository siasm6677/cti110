# CTI-110
# P3HW2 - Salary Calculator
# Maira Sias
# 10/16/2022
#
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print("----------------------------------------")
print(f'{"Employee name:":20} {employee_name}')
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
print(f'{hours_worked:<15} {pay_rate:<15} {overtime_hrs:<15} $ {overtime_pay:<13} $ {reg_hr_pay:<13} $ {gross_pay:<13}')

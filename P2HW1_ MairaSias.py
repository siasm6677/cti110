# Calculate and display travel expenses
# 9/26/2022
# CTI-110 P2HW1 - Travel
# Maira Sias
#
# Get input from user defining what their budget is, where they want to go
#    and waht their expected expenses for gas, lodging, and food will be
# Program calculates what the user's remaining balance based on user's input
# Program calculates budget minus expenses to get remaining balance
# print input with descriptions in a neat format
# print final calculation
#
print('This program calculates and displays travel expenses')
print('Enter budget:', end=' ')
budget = float(input())
print('Enter your travel destination:', end=' ')
destination = input()
print('How much do you think you will spend on gas?', end=' ')
fuel = float(input())
print('How much do you think you will spend on accomodations?', end=' ')
accomodation = float(input())
print('How much do you think you will spend on food?', end=' ')
food = float(input())
print('------------Travel Expenses------------')
print(f'{"Location:":20} {destination}')
print(f'{"Initial Budget:":20} {"$"}{budget}')
print(f'{"Fuel:":20} {"$"}{fuel}')
print(f'{"Accomodation:":20} {"$"}{accomodation}')
print(f'{"Food:":20} {"$"}{food}')
print('----------------------------------------')
print()
expenses = fuel + accomodation + food
remaining_balance = budget - expenses
print(f'{"Remaining Balance:":20} {"$"}{remaining_balance}')


# Calculate and display travel expenses
# 9/19/2022
# CTI-110 P1HW2 - Travel Expense
# Maira Sias
#

print('What is your budget?', end=' ')
budget = int(input())
print('Where do you want to go?', end=' ')
destination = input()
print('How much do you think you will sepnd on gas?', end=' ')
fuel = int(input())
print('How much do you think you will spend on accomodations?', end=' ')
accomodation = int(input())
print('How much do you think you will spend on food?', end=' ')
food = int(input())
print('------------Travel Expenses------------')
print('Location: ', destination)
print('Initial Budget: ', budget)
print()
print('Fuel: ', fuel)
print('Accomodation: ', accomodation)
print('Food: ', food)
print()
expenses = fuel + accomodation + food
remaining_balance = budget - expenses
print('Remaining Balance: ', remaining_balance)

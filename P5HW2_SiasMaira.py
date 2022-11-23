# Create a program with a starting menu that gives a user the option to add or subtract
# two random numbers or exit the program. Use a while loop to check user input answer
# and count number of attempts it took to get the correct answer. If user input is correct,
# congratulate user then display menu again. If user input is incorrect, give them a hint
# and ask for user input again until user enters corrent answer.
#
# 27 November 2022
# CTI-110 P5HW2 - Math Quiz
# Maira Sias
#

import random

def print_menu():
    print(" MAIN MENU")
    print("-"* 40)
    print(" 1. Adding Random Numbers")
    print(" 2. Subtracting Random Numbers")
    print(" 3. Exit")

def add_nums():
    print("\nSolve the equation.")
    num1 = random.randint(100, 200)
    print(" ", num1)
    num2 = random.randint(100, 200)
    print("+", num2)    
    answer = int(input("Enter answer:"))
    print()
    count = 0
    while answer != 0:
        if answer < (num1 + num2):
            print("Sorry, guess is too low.")
            answer = int(input("\nTry again: "))
            count += 1
        elif answer > (num1 + num2):
            print("Sorry, guess is too high")
            answer = int(input("\nTry again: "))
            count += 1
        else:
            if answer == (num1 + num2):
                print("Congrats! You got it right.")
                print()
                count += 1
                break  
    print("Number of attempts it took to get the right answer: ", count)
    print()

def subtract_nums():
    print("\nSolve the equation.")
    num1 = random.randint(100, 200)
    print(" ", num1)
    num2 = random.randint(0, 99)
    print("-", num2)    
    answer = int(input("Enter answer:"))
    print()
    count = 0
    while answer != 0:
        if answer < (num1 - num2):
            print("Sorry, guess is too low.")
            answer = int(input("\nTry again: "))
            count += 1
        elif answer > (num1 - num2):
            print("Sorry, guess is too high")
            answer = int(input("\nTry again: "))
            count += 1
        else:
            if answer == (num1 - num2):
                print("Congrats! You got it right.")
                print()
                count += 1
                break  
    print("Number of attempts it took to get the right answer: ", count)
    print()

exit = False

print("Welcome to Math Quiz\n")

while not exit:
    print_menu()
    print()
    choice = int(input(" Please choose one of the menu options:"))
    if choice == 3:
        print("\nThank you for playing . . . \nGoodbye!!")
        exit = True
    elif choice == 1:
        add_nums()
    elif choice == 2:
        subtract_nums()
    else:
        print("\n Please choose one of the menu options:\n")

# CTI-110
# P3HW1 - Debugging
# Maira Sias
# 10/16/2022

# This program takes a number grade, determines average and displays letter grade for average.
# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
print()
print("-------------Results-------------")
print(f'{"Lowest grade:":20} {min(grades)}')
print(f'{"Highest grade:":20} {max(grades)}')
print(f'{"Sum of grades:":20} {sum(grades)}')
print(f'{"Average: ":20} {sum(grades)/len(grades):.2f}')
print("---------------------------------")

avg = sum(grades)/len(grades)

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')






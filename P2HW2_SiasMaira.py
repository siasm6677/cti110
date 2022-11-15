# CTI-110
# P2HW2 - List
# Maira Sias
# 10/1/2022
# 
# Create a list of test grades for modules 1-6 using user input
# Show the lowest grade in the list
# Show the highest grade in the list
# Show the sum of all grades
# Show the average of all grades

grades = []
 
Mod1 = float(input("Enter grade for Module 1: "))
grades.append(Mod1)
Mod2 = float(input("Enter grade for Module 2: "))
grades.append(Mod2)
Mod3 = float(input("Enter grade for Module 3: "))
grades.append(Mod3)
Mod4 = float(input("Enter grade for Module 4: "))
grades.append(Mod4)
Mod5 = float(input("Enter grade for Module 5: "))
grades.append(Mod5)
Mod6 = float(input("Enter grade for Module 6: "))
grades.append(Mod6)
print()
print("-------------Results-------------")
print(f'{"Lowest grade:":20} {min(grades)}')
print(f'{"Highest grade:":20} {max(grades)}')
print(f'{"Sum of grades:":20} {sum(grades)}')
print(f'{"Average: ":20} {sum(grades)/len(grades):.2f}')
print("---------------------------------")

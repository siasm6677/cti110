# CTI-110
# P4HW1 - Score List
# Maira Sias
# 11/13/2022
# 
# Ask user for number of scores they would like to enter
# Create a loop to collect the number of scores using user input and add scores to a list
# Evalute is score is between 0 and 100 
# If score is invalid, remove score from the list
# Show then remove the lowest score in the list
# Show the average of the new modified list

collected_scores = []

num_scores = int(input("How many scores do you want to enter? "))

score_num = 1
for i in range(num_scores):
    print("Enter score #", score_num,": ", end=' ')
    score_num += 1
    input_score = float(input())
    collected_scores.append(input_score)
    if input_score < 0:
        collected_scores.pop()
        print()
        print("INVALID Score entered!!!!\nScore should be between 0 and 100")
        input_score = float(input("Enter score again: "))
        collected_scores.append(input_score)
    elif input_score > 100:
        collected_scores.pop()
        print()
        print("INVALID Score entered!!!!\nScore should be between 0 and 100")
        input_score = float(input("Enter score again: "))
        collected_scores.append(input_score)
        
print()
print("-------------Results-------------")
print(f'{"Lowest Score:":18} {min(collected_scores)}')
collected_scores.remove(min(collected_scores))
print(f'{"Modified List:":18} {collected_scores}')
print(f'{"Average: ":18} {sum(collected_scores)/len(collected_scores):.2f}')
avg = sum(collected_scores)/len(collected_scores)
if avg >= 90:
    print(f'{"Grade: ":18} A')
elif avg >= 80 and avg < 90:
    print(f'{"Grade: ":18} B')
elif avg >= 70 and avg < 80:
    print(f'{"Grade: ":18} C')
elif avg >= 60 and avg < 70:
    print(f'{"Grade: ":18} D')
else:
    print(f'{"Grade: ":18} F')
print("---------------------------------")



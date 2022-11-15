num_1 = int(input())
num_2 = int(input())

if num_1 <= num_2:
    while num_1 <= num_2:
        print(num_1, end=' ')
        num_1 += 5
    print()
else:
    print("Second integer can't be less than the first.")
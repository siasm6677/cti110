def days_in_feb(user_year):
    if user_year % 100 == 0:
        if user_year % 400 == 0:
            return 29
        else:
            return 28
    else:
        if user_year % 4 == 0:
            return 29
        else:
            return 28

if __name__ == '__main__':
    user_year = int(input())
    days_in_feb(user_year)
    print(user_year, 'has', days_in_feb(user_year), 'days in February.')
    # Type your code here. Your code must call the function.
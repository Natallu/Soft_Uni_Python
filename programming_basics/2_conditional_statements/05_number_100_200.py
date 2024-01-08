users_number = int(input())

if users_number < 100:
    print("Less than 100")
elif 100 <= users_number <= 200:
    print("Between 100 and 200")
elif users_number > 200:
    print("Greater than 200")

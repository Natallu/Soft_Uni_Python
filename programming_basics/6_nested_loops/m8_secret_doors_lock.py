hundreds_range = int(input())
dozens_range = int(input())
units_range = int(input())

for first_number in range(1, hundreds_range + 1):
    for second_number in range(1, dozens_range + 1):
        for third_number in range(1, units_range + 1):
            if first_number % 2 == 0 and third_number % 2 == 0:
                if second_number in (2, 3, 5, 7):
                    secret_code = f'{first_number} {second_number} {third_number}'
                    print(secret_code)

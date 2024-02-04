third_symbol_end = int(input())
fourth_symbol_end = int(input())
max_generated_passwords = int(input())

first_symbol_start = 35
first_symbol_end = 55
second_symbol_start = 64
second_symbol_end = 96


for third_symbol in range(1, third_symbol_end + 1):
    for fourth_symbol in range(1, fourth_symbol_end + 1):
        if max_generated_passwords == 0:
            break
        if first_symbol_start > first_symbol_end:
            first_symbol_start = 35
        if second_symbol_start > second_symbol_end:
            second_symbol_start = 64
        password = (f'{chr(first_symbol_start)}{chr(second_symbol_start)}{third_symbol}'
                    f'{fourth_symbol}{chr(second_symbol_start)}{chr(first_symbol_start)}|')
        max_generated_passwords -= 1
        first_symbol_start += 1
        second_symbol_start += 1
        print(password, end="")

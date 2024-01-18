first_number = int(input())
second_number = int(input())
operator = input()

result = 0
result_2 = 0

if operator in ('+', '-', '*'):
    if operator == '+':
        result = first_number + second_number
        even_odd = result % 2
        if even_odd == 0:
            result_2 = 'even'
        else:
            result_2 = 'odd'
    elif operator == '-':
        result = first_number - second_number
        even_odd = result % 2
        if even_odd == 0:
            result_2 = 'even'
        elif even_odd == 1:
            result_2 = 'odd'
    elif operator == '*':
        result = first_number * second_number
        even_odd = result % 2
        if even_odd == 0:
            result_2 = 'even'
        elif even_odd == 1:
            result_2 = 'odd'
    print(f'{first_number} {operator} {second_number} = {result} - {result_2}')
elif operator == '/':
    if second_number == 0:
        print(f'Cannot divide {first_number} by zero')
    else:
        result = first_number / second_number
        print(f'{first_number} / {second_number} = {result:.2f}')
elif operator == '%':
    if second_number == 0:
        print(f'Cannot divide {first_number} by zero')
    else:
        result = first_number % second_number
        print(f"{first_number} % {second_number} = {result}")

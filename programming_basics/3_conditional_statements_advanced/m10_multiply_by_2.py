result = 0
current_number = 0

while current_number >= 0:
    current_number = float(input())
    if current_number < 0:
        print('Negative number!')
        break

    else:
        result = current_number * 2
        print(f'Result: {result:.2f}')

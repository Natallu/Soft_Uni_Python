control_number = int(input())

counter = 0
password = 0
numbers = []

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d:
                    result = a * b + c * d
                    if result == control_number:
                        counter += 1
                        number = f'{a}{b}{c}{d}'
                        numbers.append(number)
                        if counter == 4:
                            password = number
if numbers:
    print(*numbers)

if password:
    print(f'Password: {password}')
else:
    print('No!')

data = input()

sum_prime_numbers = 0
sum_non_prime_numbers = 0

while data != 'stop':

    current_number = int(data)

    counter = 0
    for i in range(1, current_number + 1):
        if current_number % i == 0:
            counter += 1

    if current_number < 0:
        print("Number is negative.")
    elif counter == 2:
        sum_prime_numbers += current_number
    else:
        sum_non_prime_numbers += current_number

    data = input()

print(f'Sum of all prime numbers is: {sum_prime_numbers}')
print(f'Sum of all non prime numbers is: {sum_non_prime_numbers}')

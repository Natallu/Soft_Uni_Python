first_star = int(input())
second_start = int(input())
first_diff = int(input())
second_diff = int(input())

first_end = first_star + first_diff
second_end = second_start + second_diff

is_prime_first = False
is_prime_second = False

for first in range(first_star, first_end + 1):
    is_prime_first = True
    for i in range(2, first):
        if first % i == 0:
            is_prime_first = False
    if not is_prime_first:
        continue
    else:
        first_number = first

    for second in range(second_start, second_end + 1):
        is_prime_second = True
        for j in range(2, second):
            if second % j == 0:
                is_prime_second = False
        if not is_prime_second:
            continue
        else:
            second_number = second

            if is_prime_first and is_prime_second:
                print(f'{first_number}{second_number}')

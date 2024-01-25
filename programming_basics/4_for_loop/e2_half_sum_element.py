import sys

numbers = int(input())

maximum = - sys.maxsize
total = 0

for _ in range(0, numbers):
    current_number = int(input())
    if current_number > maximum:
        maximum = current_number

    total += current_number

if maximum == total - maximum:
    print('Yes')
    print(f'Sum = {maximum}')
else:
    print('No')
    other_total = total - maximum
    diff = abs(maximum - other_total)
    print(f'Diff = {diff}')

from sys import maxsize

n = int(input())

odd_minimum = maxsize
odd_maximum = - maxsize
odd_total = 0

even_minimum = maxsize
even_maximum = - maxsize
even_total = 0

for i in range(1, n + 1):
    current_number = float(input())
    if i % 2 == 0:
        even_total += current_number
        if current_number > even_maximum:
            even_maximum = current_number
        if current_number == 0 or current_number == - maxsize:
            even_maximum = 0
        if current_number < even_minimum:
            even_minimum = current_number
        if current_number == 0 or current_number == maxsize:
            even_minimum = 0
    elif i % 2 != 0:
        odd_total += current_number
        if current_number > odd_maximum:
            odd_maximum = current_number
        if current_number == 0 or current_number == - maxsize:
            odd_maximum = 0
        if current_number < odd_minimum:
            odd_minimum = current_number
        if current_number == 0 or current_number == maxsize:
            odd_minimum = 0

print(f'OddSum={odd_total:.2f},')
if (odd_maximum == 0 and odd_minimum == 0) or (odd_maximum == - maxsize and odd_minimum == maxsize):
    print(f'OddMin=No,')
    print(f'OddMax=No,')
else:
    print(f'OddMin={odd_minimum:.2f},')
    print(f'OddMax={odd_maximum:.2f},')
print(f'EvenSum={even_total:.2f},')
if (even_maximum == 0 and even_minimum == 0) or (even_maximum == - maxsize and even_minimum == maxsize):
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
else:
    print(f'EvenMin={even_minimum:.2f},')
    print(f'EvenMax={even_maximum:.2f}')

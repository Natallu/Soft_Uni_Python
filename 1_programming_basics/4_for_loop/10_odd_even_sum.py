numbers = int(input())

odd_total = 0
even_total = 0

for i in range(1, numbers + 1):
    current_number = int(input())
    if i % 2 == 0:
        even_total += current_number
    else:
        odd_total += current_number

diff = abs(odd_total - even_total)

if odd_total == even_total:
    print('Yes')
    print(f'Sum = {odd_total}')
else:
    print('No')
    print(f'Diff = {diff}')

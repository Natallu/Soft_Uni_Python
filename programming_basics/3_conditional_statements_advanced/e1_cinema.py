ticket = input()
rows = int(input())
columns = int(input())

seats = rows * columns
income = 0

if ticket == 'Premiere':
    income = seats * 12
elif ticket == 'Normal':
    income = seats * 7.5
elif ticket == 'Discount':
    income = seats * 5

print(f'{income:.2f} leva')

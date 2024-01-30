n = int(input())
counter_amount = 0

for num in range(n):
    number = int(input())
    counter_amount += number

arithmetic = counter_amount / n

print(f'{arithmetic:.2f}')

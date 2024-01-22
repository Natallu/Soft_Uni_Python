numbers = int(input())

left_total = 0
right_total = 0

for left in range(numbers):
    left_current_number = int(input())
    left_total += left_current_number

for right in range(numbers):
    right_current_number = int(input())
    right_total += right_current_number

total = left_total
diff = abs(left_total - right_total)

if left_total == right_total:
    print(f'Yes, sum = {total}')
else:
    print(f'No, diff = {diff}')

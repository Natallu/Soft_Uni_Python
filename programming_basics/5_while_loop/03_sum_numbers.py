first_number = int(input())

total = 0

while total < first_number:
    current_number = int(input())
    total += current_number
    if total >= first_number:
        print(total)
        break

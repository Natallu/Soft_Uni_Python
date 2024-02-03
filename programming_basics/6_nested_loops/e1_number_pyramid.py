number = int(input())

is_bigger_than_number = False
current_number = 1
for row in range(1, number + 1):
    for column in range(1, row + 1):

        if current_number > number:
            is_bigger_than_number = True
            break
        print(current_number, end=" ")

        current_number += 1

    if is_bigger_than_number:
        break

    print()

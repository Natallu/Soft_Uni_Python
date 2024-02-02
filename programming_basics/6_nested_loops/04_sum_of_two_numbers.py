first_range = int(input())
second_range = int(input())
magic_number = int(input())

counter = 0
flag = False
for x1 in range(first_range, second_range + 1):
    for x2 in range(first_range, second_range + 1):

        counter += 1

        if x1 + x2 == magic_number:
            flag = True
            print(f"Combination N:{counter} ({x1} + {x2} = {magic_number})")
            break

    if flag:
        break

else:
    print(f"{counter} combinations - neither equals {magic_number}")

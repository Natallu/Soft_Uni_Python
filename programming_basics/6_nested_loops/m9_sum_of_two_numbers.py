start_range = int(input())
end_range = int(input())
magic_number = int(input())

combo_counter = 0
is_magic = False

for first_number in range(start_range, end_range + 1):
    for second_number in range(start_range, end_range + 1):
        combination = first_number + second_number
        combo_counter += 1
        if combination == magic_number:
            is_magic = True
            break
    if is_magic:
        break

if is_magic:
    print(f"Combination N:{combo_counter} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combo_counter} combinations - neither equals {magic_number}")

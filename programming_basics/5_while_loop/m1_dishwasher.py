bottles_of_detergent = int(input())

available_detergent = bottles_of_detergent * 750
detergent = available_detergent
dishes_counter = 0
pots_counter = 0
counter = 0

while detergent >= 0:
    data = input()

    if data == 'End':
        break

    current_utensils = int(data)
    counter += 1

    if counter % 3 == 0:
        pots_counter += current_utensils
        detergent -= current_utensils * 15
    else:
        dishes_counter += current_utensils
        detergent -= current_utensils * 5

if detergent < 0:
    print(f'Not enough detergent, {abs(detergent)} ml. more necessary!')
else:
    print("Detergent was enough!")
    print(f'{dishes_counter} dishes and {pots_counter} pots were washed.')
    print(f'Leftover detergent {detergent} ml.')

charity_wanted_am = int(input())

cash_counter = 0 #obshto kesh
cash_number = 0 #obsht broi kesh
card_counter = 0 #obshto karta
card_number = 0 #obsht broi karta
counter = 0

while True:

    if cash_counter + card_counter >= charity_wanted_am:
        cash_average = cash_counter / cash_number
        card_average = card_counter / card_number
        print(f"Average CS: {cash_average:.2f}")
        print(f"Average CC: {card_average:.2f}")

        break

    data = input()

    if data == 'End':
        print("Failed to collect required money for charity.")

        break

    current_amount = int(data)

    counter += 1
    cash_payment = counter % 2 == 1

    if current_amount <= 100 and cash_payment:
        cash_number += 1
        cash_counter += current_amount
    elif current_amount >= 10 and not cash_payment:
        card_number += 1
        card_counter += current_amount
    else:
        print('Error in transaction!')

        continue

    print('Product sold!')

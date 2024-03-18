customers_in_shop = int(input())

items_price = {
    "basket": 1.50,
    "wreath": 3.80,
    "chocolate bunny": 7
         }

total_amount = 0

for customer in range(1, customers_in_shop + 1):

    items_count = 0
    total_price = 0

    while True:
        current_item = input()

        if current_item == 'Finish':
            if items_count % 2 == 0:
                total_price = total_price - total_price * 0.2

            print(f"You purchased {items_count} items for {total_price:.2f} leva.")
            break

        total_price += items_price[current_item]
        items_count += 1

    total_amount += total_price

average_per_user = total_amount / customers_in_shop

print(f"Average bill per client is: {average_per_user:.2f} leva.")

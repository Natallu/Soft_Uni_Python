vaucher = int(input())

data = input()

all = vaucher
ticket_counter = 0
other_purchases_counter = 0
while data != 'End':
    purchase = data

    if len(purchase) <= 8:
        price = ord(purchase[0])
        if price > all:
            break
        else:
            other_purchases_counter += 1
            all -= price
    elif len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
        if price > all:
            break
        else:
            ticket_counter += 1
            all -= price

    data = input()

print(ticket_counter)
print(other_purchases_counter)

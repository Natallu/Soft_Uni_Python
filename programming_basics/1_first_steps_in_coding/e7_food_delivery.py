chicken = int(input())
fish = int(input())
veggie = int(input())

chicken_price = chicken * 10.35
fish_price = fish * 12.40
veggie_price = veggie * 8.15
dessert = (chicken_price + fish_price + veggie_price) * 0.2

delivery = 2.50

order_price = chicken_price + fish_price + veggie_price + dessert

total_price = order_price + delivery

print(total_price)

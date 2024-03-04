from math import floor, ceil

tennis_rocket = float(input())
count_tennis_rockets = int(input())
count_snickers = int(input())

snickers_price = tennis_rocket / 6
snickers_and_rockets = snickers_price * count_snickers + count_tennis_rockets * tennis_rocket
other_equipment = snickers_and_rockets * 0.2
total_order = other_equipment + snickers_and_rockets

djokovic_to_pay = total_order / 8
sponsors_to_pay = total_order * 7/8

print(f'Price to be paid by Djokovic {floor(djokovic_to_pay)}\nPrice to be paid by sponsors {ceil(sponsors_to_pay)}')

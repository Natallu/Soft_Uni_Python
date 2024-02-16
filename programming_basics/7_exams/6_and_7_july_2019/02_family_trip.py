budget = float(input())
count_nights = int(input())
price_per_night = float(input())
additional_expenses_percents = int(input())

additional_expenses_price = additional_expenses_percents / 100 * budget

total_nights_cost = 0
if count_nights > 7:
    discount = price_per_night * 0.05
    one_night = price_per_night - discount
    total_nights_cost = count_nights * one_night
else:
    total_nights_cost = count_nights * price_per_night

total_expenses = total_nights_cost + additional_expenses_price

diff = abs(total_expenses - budget)
if budget >= total_expenses:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")

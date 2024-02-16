beverage_type = input()
sugar = input()
count_beverages = int(input())
total = 0

if sugar == 'Without':
    discount = 0.35
    if beverage_type == 'Espresso':
        total = count_beverages * 0.90 - (count_beverages * 0.90 * discount)
        if count_beverages >= 5:
            total = total - total * 0.25
    elif beverage_type == 'Cappuccino':
        total = count_beverages * 1 - (count_beverages * 1 * discount)
    elif beverage_type == 'Tea':
        total = count_beverages * 0.50 - (count_beverages * 0.50 * discount)

elif sugar == 'Normal':
    if beverage_type == 'Espresso':
        total = count_beverages * 1
        if count_beverages >= 5:
            total = total - total * 0.25
    elif beverage_type == 'Cappuccino':
        total = count_beverages * 1.20
    elif beverage_type == 'Tea':
        total = count_beverages * 0.60

elif sugar == 'Extra':
    if beverage_type == 'Espresso':
        total = count_beverages * 1.20
        if count_beverages >= 5:
            total = total - total * 0.25
    elif beverage_type == 'Cappuccino':
        total = count_beverages * 1.60
    elif beverage_type == 'Tea':
        total = count_beverages * 0.70

final_price = 0
if total > 15:
    final_price = total - total * 0.2
else:
    final_price = total

print(f'You bought {count_beverages} cups of {beverage_type} for {final_price:.2f} lv.')

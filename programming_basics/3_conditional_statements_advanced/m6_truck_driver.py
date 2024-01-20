season = input()
km_per_month = float(input())

months_per_season = 4
price_per_km = 0

if km_per_month <= 5000:
    if season in ('Spring', 'Autumn'):
        price_per_km = 0.75
    elif season == 'Summer':
        price_per_km = 0.9
    elif season == 'Winter':
        price_per_km = 1.05
elif 5000 < km_per_month <= 10000:
    if season in ('Spring', 'Autumn'):
        price_per_km = 0.95
    elif season == 'Summer':
        price_per_km = 1.10
    elif season == 'Winter':
        price_per_km = 1.25
elif 10000 < km_per_month <= 20000:
    if season in ('Spring', 'Summer', 'Autumn', 'Winter'):
        price_per_km = 1.45

salary = km_per_month * price_per_km * months_per_season
salary_after_tax = salary - salary * 0.1

print(f'{salary_after_tax:.2f}')

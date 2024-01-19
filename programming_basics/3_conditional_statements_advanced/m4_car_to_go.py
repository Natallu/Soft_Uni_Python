budget = float(input())
season = input()

class_type = 0
#Economy class, Compact class, Luxury class
car_type = 0
#Cabrio, Jeep
car_price = 0

if budget <= 100:
    class_type = 'Economy class'
    if season == 'Summer':
        car_type = 'Cabrio'
        car_price = budget * 0.35
    elif season == 'Winter':
        car_type = 'Jeep'
        car_price = budget * 0.65
elif 100 < budget <= 500:
    class_type = 'Compact class'
    if season == 'Summer':
        car_type = 'Cabrio'
        car_price = budget * 0.45
    elif season == 'Winter':
        car_type = 'Jeep'
        car_price = budget * 0.8
elif budget > 500:
    class_type = 'Luxury class'
    if season in ('Summer', 'Winter'):
        car_type = 'Jeep'
        car_price = budget * 0.9

print(class_type)
print(f'{car_type} - {car_price:.2f}')

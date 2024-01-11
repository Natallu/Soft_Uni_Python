kilometers = int(input())
day_or_night = input()

price_trip = 0

if kilometers < 20:
    if day_or_night == 'day':
        price_trip = 0.70 + kilometers * 0.79
    elif day_or_night == 'night':
        price_trip = 0.70 + kilometers * 0.90
elif 20 <= kilometers < 100:
    price_trip = kilometers * 0.09
else:
    price_trip = kilometers * 0.06

print(f'{price_trip:.2f}')

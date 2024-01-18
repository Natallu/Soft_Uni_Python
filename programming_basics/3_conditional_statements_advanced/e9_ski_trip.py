days = int(input())
place_type = input()
feedback = input()

nights = days - 1
room_price = nights * 18
apartment_price = nights * 25
president_apartment_price = nights * 35
price = 0

if place_type == 'room for one person':
    price = room_price
elif place_type == 'apartment':
    if nights <= 10:
        price = apartment_price - apartment_price * 0.3
    elif 10 < nights <= 15:
        price = apartment_price - apartment_price * 0.35
    elif nights > 15:
        price = apartment_price - apartment_price * 0.5
elif place_type == 'president apartment':
    if nights <= 10:
        price = president_apartment_price - president_apartment_price * 0.1
    elif 10 < nights <= 15:
        price = president_apartment_price - president_apartment_price * 0.15
    elif nights > 15:
        price = president_apartment_price - president_apartment_price * 0.2

feedback_price = 0

if feedback == 'positive':
    feedback_price = price + price * 0.25
elif feedback == 'negative':
    feedback_price = price - price * 0.1

print(f'{feedback_price:.2f}')

season = input()
group_type = input()
students = int(input())
nights = int(input())

price_per_person = 0
sports_type = 0

if season == 'Winter':
    if group_type == 'girls':
        sports_type = 'Gymnastics'
        price_per_person = 9.60
    elif group_type == 'boys':
        sports_type = 'Judo'
        price_per_person = 9.60
    elif group_type == 'mixed':
        sports_type = 'Ski'
        price_per_person = 10
elif season == 'Spring':
    if group_type == 'girls':
        sports_type = 'Athletics'
        price_per_person = 7.20
    elif group_type == 'boys':
        sports_type = 'Tennis'
        price_per_person = 7.20
    elif group_type == 'mixed':
        sports_type = 'Cycling'
        price_per_person = 9.50
elif season == 'Summer':
    if group_type == 'girls':
        sports_type = 'Volleyball'
        price_per_person = 15
    elif group_type == 'boys':
        sports_type = 'Football'
        price_per_person = 15
    elif group_type == 'mixed':
        sports_type = 'Swimming'
        price_per_person = 20

discount = 0

if students < 10:
    discount = 0
elif 10 <= students < 20:
    discount = 0.05
elif 20 >= students < 50:
    discount = 0.15
elif 50 <= students:
    discount = 0.5

vacation_price = students * price_per_person * nights
discount_price = vacation_price * discount
final_price = vacation_price - discount_price

print(f'{sports_type} {final_price:.2f} lv.')

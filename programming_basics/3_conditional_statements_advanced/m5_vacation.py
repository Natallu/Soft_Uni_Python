budget = float(input())
season = input()

location = 0
#Alaska, Morocco
accomoodation_type = 0
#Hotel, Hut, Camp
vacation_price = 0

if budget <= 1000:
    accomoodation_type = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        vacation_price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        vacation_price = budget * 0.45
elif 1000 < budget <= 3000:
    accomoodation_type = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        vacation_price = budget * 0.8
    elif season == 'Winter':
        location = 'Morocco'
        vacation_price = budget * 0.6
elif budget > 3000:
    accomoodation_type = 'Hotel'
    if season == 'Summer':
        location = 'Alaska'
        vacation_price = budget * 0.9
    elif season == 'Winter':
        location = 'Morocco'
        vacation_price = budget * 0.9

print(f'{location} - {accomoodation_type} - {vacation_price:.2f}')

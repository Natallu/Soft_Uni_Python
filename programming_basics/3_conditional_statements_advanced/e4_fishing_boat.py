budget = int(input())
season = input()
fishermen = int(input())

rent = 0

if season == 'Spring':
    if fishermen <= 6:
        rent = 3000 - 3000 * 0.1
    elif 7 <= fishermen <= 11:
        rent = 3000 - 3000 * 0.15
    elif fishermen >= 12:
        rent = 3000 - 3000 * 0.25
elif season == "Summer" or season == 'Autumn':
    if fishermen <= 6:
        rent = 4200 - 4200 * 0.1
    elif 7 <= fishermen <= 11:
        rent = 4200 - 4200 * 0.15
    elif fishermen >= 12:
        rent = 4200 - 4200 * 0.25
elif season == 'Winter':
    if fishermen <= 6:
        rent = 2600 - 2600 * 0.1
    elif 7 <= fishermen <= 11:
        rent = 2600 - 2600 * 0.15
    elif fishermen >= 12:
        rent = 2600 - 2600 * 0.25

discount = fishermen % 2
rent_discount = 0

if discount == 0:
    if season in ("Spring", "Summer", "Winter"):
        rent_discount = rent - rent * 0.05
if season == 'Autumn' or discount == 1:
    rent_discount = rent

diff = abs(budget - rent_discount)

if budget >= rent_discount:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")

holiday_month = input()
nights_to_stay = int(input())

apartment_price = 0
studio_price = 0

if holiday_month == 'May' or holiday_month == 'October':
    if nights_to_stay <= 7:
        studio_price = nights_to_stay * 50
        apartment_price = nights_to_stay * 65
    elif 7 < nights_to_stay <= 14:
        studio_price = nights_to_stay * 50 - (nights_to_stay * 50 * 0.05)
        apartment_price = nights_to_stay * 65
    elif nights_to_stay > 14:
        studio_price = nights_to_stay * 50 - (nights_to_stay * 50 * 0.3)
        apartment_price = nights_to_stay * 65 - (nights_to_stay * 65 * 0.1)
elif holiday_month == 'June' or holiday_month == 'September':
    if nights_to_stay <= 14:
        studio_price = nights_to_stay * 75.2
        apartment_price = nights_to_stay * 68.7
    elif nights_to_stay > 14:
        studio_price = nights_to_stay * 75.2 - (nights_to_stay * 75.2 * 0.2)
        apartment_price = nights_to_stay * 68.7 - (nights_to_stay * 68.7 * 0.1)
elif holiday_month == 'July' or holiday_month == 'August':
    if nights_to_stay <= 14:
        studio_price = nights_to_stay * 76
        apartment_price = nights_to_stay * 77
    elif nights_to_stay > 14:
        studio_price = nights_to_stay * 76
        apartment_price = nights_to_stay * 77 - (nights_to_stay * 77 * 0.1)

print(f'Apartment: {apartment_price:.2f} lv.')
print(f"Studio: {studio_price:.2f} lv.")

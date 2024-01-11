fuel_type = input()
fuel_liters = float(input())
club_card = input()

gasoline = fuel_liters * 2.22
diesel = fuel_liters * 2.33
gas = fuel_liters * 0.93

total_price = 0
if club_card == 'Yes':
    if fuel_type == 'Gasoline':
        total_price = gasoline - fuel_liters * 0.18
    elif fuel_type == 'Diesel':
        total_price = diesel - fuel_liters * 0.12
    elif fuel_type == 'Gas':
        total_price = gas - fuel_liters * 0.08
elif club_card == 'No':
    if fuel_type == 'Gasoline':
        total_price = gasoline
    elif fuel_type == 'Diesel':
        total_price = diesel
    elif fuel_type == 'Gas':
        total_price = gas

if 20 <= fuel_liters <= 25:
    total_price = total_price - total_price * 0.08
elif 25 < fuel_liters:
    total_price = total_price - total_price * 0.1

print(f'{total_price:.2f} lv.')

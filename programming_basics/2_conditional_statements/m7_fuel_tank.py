fuel_type = input()
available_liters = float(input())

if available_liters < 25:
    if fuel_type == 'Diesel':
        print(f'Fill your tank with diesel!')
    elif fuel_type == 'Gasoline':
        print(f'Fill your tank with gasoline!')
    elif fuel_type == 'Gas':
        print(f'Fill your tank with gas!')
    else:
        print('Invalid fuel!')
elif available_liters >= 25:
    if fuel_type == 'Diesel':
        print(f'You have enough diesel.')
    elif fuel_type == 'Gasoline':
        print(f'You have enough gasoline.')
    elif fuel_type == 'Gas':
        print(f'You have enough gas.')
    else:
        print('Invalid fuel!')

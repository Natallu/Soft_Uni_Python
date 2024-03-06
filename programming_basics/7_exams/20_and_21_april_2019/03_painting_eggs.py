def calculate_income(egg_size, egg_color, batches):
    egg_prices = {
        'Large': {'Red': 16, 'Green': 12, 'Yellow': 9},
        'Medium': {'Red': 13, 'Green': 9, 'Yellow': 7},
        'Small': {'Red': 9, 'Green': 8, 'Yellow': 5}
    }

    production_costs_percentage = 0.35

    egg_price = egg_prices[egg_size][egg_color]
    total_income = batches * egg_price
    total_income_after_costs = total_income * (1 - production_costs_percentage)

    return total_income_after_costs


egg_size = input()
egg_color = input()
batches = int(input())

total_income = calculate_income(egg_size, egg_color, batches)

print(f"{total_income:.2f} leva.")

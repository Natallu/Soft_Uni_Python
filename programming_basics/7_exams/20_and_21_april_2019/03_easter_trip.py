def calculate_trip_cost(destination, dates, nights):
    destinations_prices = {
        'France': {'21-23': 30, '24-27': 35, '28-31': 40},
        'Italy': {'21-23': 28, '24-27': 32, '28-31': 39},
        'Germany': {'21-23': 32, '24-27': 37, '28-31': 43}
    }

    cost_per_night = destinations_prices[destination][dates]
    total_cost = nights * cost_per_night
    return total_cost

destination = input()
dates = input()
nights = int(input())

total_cost = calculate_trip_cost(destination, dates, nights)

print(f"Easter trip to {destination} : {total_cost:.2f} leva.")

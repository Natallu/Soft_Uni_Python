budget = float(input())
season = input()

trip_price = 0
destination = 0
trip_type = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        trip_type = 'Camp'
        trip_price = budget * 0.3
    elif season == 'winter':
        trip_type = 'Hotel'
        trip_price = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        trip_type = 'Camp'
        trip_price = budget * 0.4
    elif season == 'winter':
        trip_type = 'Hotel'
        trip_price = budget * 0.8
elif budget > 1000:
    trip_type = "Hotel"
    destination = 'Europe'
    if season == 'summer' or season == 'winter':
        trip_price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{trip_type} - {trip_price:.2f}")

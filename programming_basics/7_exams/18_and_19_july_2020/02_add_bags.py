bag_price_above_20kg = float(input())
bag_kg = float(input())
days_till_trip = int(input())
bags_count = int(input())

total_cost = 0
price_per_bag = 0

if bag_kg < 10:
    price_per_bag = bag_price_above_20kg * 0.2

elif 10 <= bag_kg <= 20:
    price_per_bag = bag_price_above_20kg / 2

elif bag_kg > 20:
    price_per_bag = bag_price_above_20kg

if days_till_trip < 7:
    total_cost = bags_count * (price_per_bag + price_per_bag * 0.4)

elif 7 <= days_till_trip <= 30:
    total_cost = bags_count * (price_per_bag + price_per_bag * .15)

elif days_till_trip > 30:
    total_cost = bags_count * (price_per_bag + price_per_bag * 0.1)

print(f"The total price of bags is: {total_cost:.2f} lv.")

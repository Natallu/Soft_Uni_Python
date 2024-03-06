number_of_guests = int(input())
price_per_person = float(input())
budget = float(input())

cake = budget * 0.1
new_price_per_person = 0

if 10 <= number_of_guests <= 15:
    new_price_per_person = price_per_person - price_per_person * 0.15

elif 15 < number_of_guests <= 20:
    new_price_per_person = price_per_person - price_per_person * 0.2

elif 20 < number_of_guests:
    new_price_per_person = price_per_person - price_per_person * .25

else:
    new_price_per_person = price_per_person

total_cost = number_of_guests * new_price_per_person + cake
diff = budget - total_cost

if total_cost <= budget:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {abs(diff):.2f} leva needed.")

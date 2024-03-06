from math import ceil

guests = int(input())
budget = float(input())

easter_bread_price = 4
egg_price = 0.45

eggs_needed_price = guests * egg_price * 2
easter_bread_needed_price = ceil(guests / 3) * easter_bread_price
total_cost = eggs_needed_price + easter_bread_needed_price
diff = budget - total_cost

if budget >= total_cost:
    print(f"Lyubo bought {ceil(guests / 3)} Easter bread and {guests * 2} eggs.")
    print(f"He has {diff:.2f} lv. left.")

else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {abs(diff):.2f} lv. more.")

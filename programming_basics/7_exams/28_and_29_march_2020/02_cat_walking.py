minutes_per_walk = int(input())
walks_per_day = int(input())
calories_per_day = int(input())

total_burned_calories = minutes_per_walk * walks_per_day * 5
percentage_burned = (total_burned_calories / calories_per_day) * 100

if percentage_burned >= 50:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories}.")

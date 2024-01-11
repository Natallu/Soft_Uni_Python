import math

days = int(input())
food_kg = int(input())
dog_per_day_kg = float(input())
cat_per_day_kg = float(input())
tortoise_per_day_gr = float(input())

dog_total_food = dog_per_day_kg * days
cat_total_food = cat_per_day_kg * days
tortoise_total_food = (tortoise_per_day_gr * days) / 1000

total_food = dog_total_food + cat_total_food + tortoise_total_food
food_left = abs(food_kg - total_food)

if food_kg >= total_food:
    print(f"{math.floor(food_left)} kilos of food left.")
else:
    print(f'{math.ceil(food_left)} more kilos of food are needed.')

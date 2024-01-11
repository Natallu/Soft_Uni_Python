import math

grapes_area_sq_m = int(input())
grapes_kg_per_sq_m = float(input())
needed_wine_l = int(input())
workers = int(input())

total_harvested_grape = grapes_area_sq_m * grapes_kg_per_sq_m
grapes_for_wine = total_harvested_grape * 0.4
wine_liters = grapes_for_wine / 2.5

wine_left = abs(wine_liters - needed_wine_l)
wine_for_workers = wine_left / workers

if wine_liters >= needed_wine_l:
    print(f'Good harvest this year! Total wine: {math.floor(wine_liters)} liters.')
    print(f'{math.ceil(wine_left)} liters left -> {math.ceil(wine_for_workers)} liters per person.')
else:
    print(f'It will be a tough winter! More {math.floor(wine_left)} liters wine needed.')

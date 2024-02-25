fruit = input()
set_size = input()
sets_count = int(input())

price_per_set = 0

if set_size == "small":
    if fruit == "Watermelon":
        price_per_set = 2 * 56
    elif fruit == "Mango":
        price_per_set = 2 * 36.66
    elif fruit == "Pineapple":
        price_per_set = 2 * 42.10
    elif fruit == "Raspberry":
        price_per_set = 2 * 20
elif set_size == "big":
    if fruit == "Watermelon":
        price_per_set = 5 * 28.70
    elif fruit == "Mango":
        price_per_set = 5 * 19.60
    elif fruit == "Pineapple":
        price_per_set = 5 * 24.80
    elif fruit == "Raspberry":
        price_per_set = 5 * 15.20

total_price = price_per_set * sets_count

if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.5

print(f"{total_price:.2f} lv.")

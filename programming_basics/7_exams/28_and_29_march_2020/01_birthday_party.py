hall_rent = float(input())

if 100 <= hall_rent <= 10000:
    cake_price = 0.2 * hall_rent
    drinks_price = 0.55 * cake_price
    animator_price = hall_rent / 3

    total_budget = hall_rent + cake_price + drinks_price + animator_price

    print(f"{total_budget:.2f}")

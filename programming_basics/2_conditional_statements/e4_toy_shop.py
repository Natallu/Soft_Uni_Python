trip_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
t_bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

puzzle_price = puzzle_count * 2.6
doll_price = doll_count * 3
t_bear_price = t_bear_count * 4.1
minion_price = minion_count * 8.2
truck_price = truck_count * 2

total_price = puzzle_price + doll_price + t_bear_price + minion_price + truck_price
total_count = puzzle_count + doll_count + t_bear_count + minion_count + truck_count

if total_count >= 50:
    total_price = total_price - total_price * 0.25

rent = total_price * 0.1
money_in_account = total_price - rent

if money_in_account >= trip_price:
    total = money_in_account - trip_price
    print(f"Yes! {total:.2f} lv left.")
else:
    total = trip_price - money_in_account
    print(f"Not enough money! {total:.2f} lv needed.")

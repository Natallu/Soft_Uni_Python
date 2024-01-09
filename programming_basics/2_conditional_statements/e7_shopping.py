budget = float(input())
video_count = int(input())
cpu_count = int(input())
ram_count = int(input())

video_price = 250 * video_count
cpu_price = cpu_count * (video_price * 0.35)
ram_price = ram_count * (video_price * 0.1)

total_price = video_price + cpu_price + ram_price

if video_count > cpu_count:
    total_price = total_price - total_price * 0.15

final_amount = 0

if budget >= total_price:
    final_amount = budget - total_price
    print(f'You have {final_amount:.2f} leva left!')
else:
    final_amount = total_price - budget
    print(f'Not enough money! You need {final_amount:.2f} leva more!')

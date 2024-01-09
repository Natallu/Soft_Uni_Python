hours = int(input())
minutes = int(input())

future_time_mins = hours * 60 + minutes + 15

total_future_hours = future_time_mins // 60
total_future_mins = future_time_mins % 60

if total_future_hours > 23:
    total_future_hours = 0

if total_future_mins < 10:
    print(f'{total_future_hours}:0{total_future_mins}')
else:
    print(f'{total_future_hours}:{total_future_mins}')

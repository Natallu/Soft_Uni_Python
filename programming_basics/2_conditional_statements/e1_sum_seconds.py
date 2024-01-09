from math import floor

t_first_player = int(input())
t_second_player = int(input())
t_third_player = int(input())

total_time = t_first_player + t_second_player + t_third_player
total_mins = total_time // 60
total_secs = total_time % 60

time_mins = floor(total_mins)

if total_secs < 10:
    print(f'{time_mins}:0{total_secs}')
else:
    print(f'{time_mins}:{total_secs}')

from math import ceil

movie_name = input()
movie_duration = int(input())
break_duration = int(input())

lunch = break_duration * 1/8
relax = break_duration * 1/4

time_left = break_duration - lunch - relax

time = 0
if time_left >= movie_duration:
    time = ceil(time_left - movie_duration)
    print(f'You have enough time to watch {movie_name} and left with {time} minutes free time.')
else:
    time = ceil(movie_duration - time_left)
    print(f"You don't have enough time to watch {movie_name}, you need {time} more minutes.")

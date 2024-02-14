from sys import maxsize

movies_number = int(input())

max = - maxsize
max_movie = 0
min = maxsize
min_movie = 0

stats = 0

for _ in range(movies_number):
    movie_name = input()
    rating = float(input())

    stats += rating

    if rating > max:
        max = rating
        max_movie = movie_name
    elif rating < min:
        min = rating
        min_movie = movie_name

average_stats = stats / movies_number
print(f'{max_movie} is with highest rating: {max:.1f}')
print(f'{min_movie} is with lowest rating: {min:.1f}')
print(f'Average rating: {average_stats:.1f}')

from math import floor

n_tournaments = int(input())
starting_points = int(input())
counter = 0
winnings = 0
points = 0

for _ in range(n_tournaments):
    results = input()
    counter += 1
    if results == 'W':
        winnings += 1
        points += 2000
    elif results == 'F':
        points += 1200
    elif results == 'SF':
        points += 720

average_points = points / counter
win_percent = winnings / counter * 100
final_points = starting_points + points

print(f'Final points: {final_points}')
print(f'Average points: {floor(average_points)}')
print(f'{win_percent:.2f}%')

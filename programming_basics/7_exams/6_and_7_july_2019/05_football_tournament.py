team_name = input()
played_games = int(input())

points = 0
wins = 0
lose = 0
draw = 0

if played_games == 0:
    print(f"{team_name} hasn't played any games during this season.")

for result in range(played_games):
    current_result = input()

    if current_result == 'W':
        wins += 1
        points += 3
    elif current_result == 'D':
        draw += 1
        points += 1
    elif current_result == 'L':
        lose += 1

if played_games > 0:
    win_rate = wins / played_games * 100
    print(f"{team_name} has won {points} points during this season.")
    print("Total stats:")
    print(f'## W: {wins}')
    print(f'## D: {draw}')
    print(f'## L: {lose}')
    print(f'Win rate: {win_rate:.2f}%')

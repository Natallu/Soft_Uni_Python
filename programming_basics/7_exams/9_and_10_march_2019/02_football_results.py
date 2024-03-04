won = 0
lost = 0
draw = 0

for game in range(1, 4):
    result = input().split(":")

    if int(result[0]) > int(result[1]):
        won += 1
    elif int(result[0]) < int(result[1]):
        lost += 1
    else:
        draw += 1

print(f"Team won {won} games.\nTeam lost {lost} games.\nDrawn games: {draw}")

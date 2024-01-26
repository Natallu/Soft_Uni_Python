game_steps = int(input())

points = 0
row_1, row_2, row_3, row_4, row_5, invalid = 0, 0, 0, 0, 0, 0

for n in range(game_steps):
    num = int(input())
    if 0 <= num <= 9:
        points += num * 0.2
        row_1 += 1
    elif 10 <= num <= 19:
        points += num * 0.3
        row_2 += 1
    elif 20 <= num <= 29:
        points += num * 0.4
        row_3 += 1
    elif 30 <= num <= 39:
        points += 50
        row_4 += 1
    elif 40 <= num <= 50:
        points += 100
        row_5 += 1
    else:
        points = points / 2
        invalid += 1

row_1_percent = row_1 / game_steps * 100
row_2_percent = row_2 / game_steps * 100
row_3_percent = row_3 / game_steps * 100
row_4_percent = row_4 / game_steps * 100
row_5_percent = row_5 / game_steps * 100
invalid_percent = invalid / game_steps * 100

print(f'{points:.2f}')
print(f'From 0 to 9: {row_1_percent:.2f}%')
print(f'From 10 to 19: {row_2_percent:.2f}%')
print(f'From 20 to 29: {row_3_percent:.2f}%')
print(f'From 30 to 39: {row_4_percent:.2f}%')
print(f'From 40 to 50: {row_5_percent:.2f}%')
print(f'Invalid numbers: {invalid_percent:.2f}%')

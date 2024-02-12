number_of_balls = int(input())

total_points = 0
colors = {
    "red": 0,
    "orange": 0,
    "yellow": 0,
    "white": 0,
    "black": 0,
    "other": 0
}

for ball in range(number_of_balls):
    color = input()

    if color == 'red':
        total_points += 5
        colors[color] += 1

    elif color == 'orange':
        total_points += 10
        colors[color] += 1

    elif color == 'yellow':
        total_points += 15
        colors[color] += 1

    elif color == 'white':
        total_points += 20
        colors[color] += 1

    elif color == 'black':
        total_points //= 2
        colors[color] += 1

    else:
        colors['other'] += 1

print(f"Total points: {total_points}")
print(f"Red balls: {colors['red']}")
print(f"Orange balls: {colors['orange']}")
print(f"Yellow balls: {colors['yellow']}")
print(f"White balls: {colors['white']}")
print(f"Other colors picked: {colors['other']}")
print(f"Divides from black balls: {colors['black']}")

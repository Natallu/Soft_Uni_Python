player_name = input()

successful_shots = 0
unsuccessful_shots = 0
current_points = 301

while True:
    field = input()

    if field == "Retire":
        print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
        break

    points = int(input())

    if field == "Single":
        points *= 1
    elif field == "Double":
        points *= 2
    elif field == "Triple":
        points *= 3

    if current_points - points < 0:
        unsuccessful_shots += 1
    else:
        successful_shots += 1
        current_points -= points

    if current_points == 0:
        print(f"{player_name} won the leg with {successful_shots} shots.")
        break

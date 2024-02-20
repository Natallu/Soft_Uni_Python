best_player_score = 0
best_player_name = ''

while True:
    name = input()

    if name == 'Stop':
        break

    current_player_score = 0
    for letter in name:
        current_number = int(input())

        if current_number == ord(letter):
            current_player_score += 10
        else:
            current_player_score += 2

    if current_player_score >= best_player_score:
        best_player_name = name
        best_player_score = current_player_score

print(f'The winner is {best_player_name} with {best_player_score} points!')

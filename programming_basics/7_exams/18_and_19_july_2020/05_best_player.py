best_player = ''
best_score = 0
is_hattrick = False

player = input()
while player != "END":

    goals = int(input())

    if goals > best_score:
        best_score = goals
        best_player = player

    if goals >= 3:
        is_hattrick = True

    if goals >= 10:
        break

    player = input()

print(f"{best_player} is the best player!")

if is_hattrick:
    print(f"He has scored {best_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_score} goals.")

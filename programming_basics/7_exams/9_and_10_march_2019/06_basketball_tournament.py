total_wins = 0
total_losses = 0

while True:
    tournament_name = input()
    if tournament_name == "End of tournaments":
        break

    total_matches = int(input())
    wins = 0
    losses = 0

    for match in range(total_matches):
        desis_points = int(input())
        opponents_points = int(input())

        if desis_points > opponents_points:
            wins += 1
            print(f"Game {match + 1} of tournament {tournament_name}: win with {desis_points - opponents_points} points.")
        else:
            losses += 1
            print(f"Game {match + 1} of tournament {tournament_name}: lost with {opponents_points - desis_points} points.")

    total_wins += wins
    total_losses += losses

total_matches_played = total_wins + total_losses
percentage_wins = (total_wins / total_matches_played) * 100
percentage_losses = (total_losses / total_matches_played) * 100

print(f"{percentage_wins:.2f}% matches win")
print(f"{percentage_losses:.2f}% matches lost")

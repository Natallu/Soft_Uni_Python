def charity_tournament(days):
    total_money = 0
    total_wins = 0
    total_losses = 0

    for day in range(1, days + 1):
        sport = input()

        daily_wins = 0
        daily_losses = 0
        daily_money = 0

        while sport != "Finish":
            result = input()
            if result == "win":
                daily_wins += 1
                daily_money += 20
            elif result == "lose":
                daily_losses += 1

            sport = input()

        if daily_wins > daily_losses:
            daily_money *= 1.1

        total_money += daily_money
        total_wins += daily_wins
        total_losses += daily_losses

    if total_wins > total_losses:
        total_money *= 1.2
        result_message = f"You won the tournament! Total raised money: {total_money:.2f}"
    else:
        result_message = f"You lost the tournament! Total raised money: {total_money:.2f}"

    return result_message


tournament_days = int(input())
result = charity_tournament(tournament_days)
print(result)

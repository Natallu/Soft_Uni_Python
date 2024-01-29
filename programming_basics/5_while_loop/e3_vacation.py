money_for_trip = float(input())
available_money = float(input())

total_days = 0
consecutive_spent_days = 0

while available_money < money_for_trip and consecutive_spent_days < 5:

    action = input()
    current_amount = float(input())
    total_days += 1

    if action == 'spend':
        available_money -= current_amount
        consecutive_spent_days += 1
        if available_money < 0:
            available_money = 0

    elif action == 'save':
        available_money += current_amount
        consecutive_spent_days = 0

if consecutive_spent_days == 5:
    print("You can't save the money.")
    print(total_days)

if available_money >= money_for_trip:
    print(f'You saved the money for {total_days} days.')

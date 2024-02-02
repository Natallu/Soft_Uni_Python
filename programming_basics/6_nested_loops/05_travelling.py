data = input()
available_money = 0
flag = False

while data != 'End':
    destination = data
    needed_money = float(input())
    while needed_money > available_money:
        data = input()

        if data != 'End':
            current_amount = float(data)
            available_money += current_amount
        else:
            flag = True

        if available_money >= needed_money:
            available_money = 0
            print(f'Going to {destination}!')
            break

    if flag:
        break

    data = input()

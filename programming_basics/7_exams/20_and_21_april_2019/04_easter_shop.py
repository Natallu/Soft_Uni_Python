initial_eggs = int(input())
total_sold_eggs = 0

while True:
    command = input()

    if command == "Close":
        print("Store is closed!")
        print(f"{total_sold_eggs} eggs sold.")
        break

    action = command
    eggs = int(input())

    if action == "Buy":
        if eggs > initial_eggs:
            print("Not enough eggs in store!")
            print(f"You can buy only {initial_eggs}.")
            break

        initial_eggs -= eggs
        total_sold_eggs += eggs

    elif action == "Fill":
        initial_eggs += eggs

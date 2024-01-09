budget = float(input())
extra_actors = int(input())
extra_actor_costume = float(input())

decor = budget * 0.1
price_costumes = extra_actors * extra_actor_costume
costume_total = 0

if extra_actors > 150:
    costume_total = price_costumes - price_costumes * 0.1
else:
    costume_total = price_costumes

total_budget = decor + costume_total

if total_budget <= budget:
    final = budget - total_budget
    print("Action!")
    print(f"Wingard starts filming with {final:.2f} leva left.")
else:
    final = total_budget - budget
    print("Not enough money!")
    print(f"Wingard needs {final:.2f} leva more.")

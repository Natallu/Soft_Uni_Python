wanted_outcome = float(input())
data = input()

income = 0
while data != "Party!":
    cocktail_name = data
    cocktail_count = int(input())

    cocktail_price = len(cocktail_name) * cocktail_count

    if cocktail_price % 2 != 0:
        cocktail_price = cocktail_price - 0.25 * cocktail_price

    income += cocktail_price

    if income >= wanted_outcome:
        break

    data = input()

diff = abs(wanted_outcome - income)
if data == 'Party!' or income < wanted_outcome:
    print(f"We need {diff:.2f} leva more.")
elif income >= wanted_outcome:
    print("Target acquired.")

print(f"Club income - {income:.2f} leva.")

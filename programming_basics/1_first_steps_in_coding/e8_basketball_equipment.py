annual_basketball_training_tax = int(input())

snickers = annual_basketball_training_tax - (annual_basketball_training_tax * 0.4)
clothes = snickers - (snickers * 0.2)
ball = 0.25 * clothes
accessories = 0.2 * ball

total_equipment = snickers + clothes + ball + accessories

total_training_expenses = annual_basketball_training_tax + total_equipment

print(total_training_expenses)

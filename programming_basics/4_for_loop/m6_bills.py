months = int(input())

electricity_bill = 0
other_expenses = 0
water_bill = months * 20
internet_bill = months * 15

for _ in range(months):
    current_bill = float(input())
    electricity_bill += current_bill
    other = 20 + 15 + current_bill
    other_expenses += other + other * 0.2

average_expenses = (water_bill + internet_bill + electricity_bill + other_expenses) / months

print(f'Electricity: {electricity_bill:.2f} lv')
print(f'Water: {water_bill:.2f} lv')
print(f'Internet: {internet_bill:.2f} lv')
print(f'Other: {other_expenses:.2f} lv')
print(f'Average: {average_expenses:.2f} lv')

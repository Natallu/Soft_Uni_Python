days = int(input())
hours = int(input())

price_per_hour = 0
bill_per_day = 0
parking_bill = 0

for days in range(1, days + 1):
    for hours in range(1, hours + 1):
        if days % 2 == 0 and hours % 2 != 0:
            price_per_hour = 2.50
        elif days % 2 != 0 and hours % 2 == 0:
            price_per_hour = 1.25
        else:
            price_per_hour = 1
        bill_per_day += price_per_hour
    print(f'Day: {days} - {bill_per_day:.2f} leva')
    parking_bill += bill_per_day
    bill_per_day = 0

print(f"Total: {parking_bill:.2f} leva")

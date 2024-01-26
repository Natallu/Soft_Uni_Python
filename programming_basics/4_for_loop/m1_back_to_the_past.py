money = float(input())
year = int(input())
ivanchos_age = 17

spent = 0

for year in range(1800, year + 1):
    ivanchos_age += 1
    if year % 2 == 0:
        spent += 12000
    elif year % 2 != 0:
        spent += 12000 + 50 * ivanchos_age

diff = abs(money - spent)

if money >= spent:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")

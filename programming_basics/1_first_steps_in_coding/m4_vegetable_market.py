veggies_price_per_kg = float(input())
fruits_price_per_kg = float(input())
veggies_total_kg = int(input())
fruits_total_kg = int(input())

veggies_total_price_lv = veggies_price_per_kg * veggies_total_kg
fruits_total_price_lv = fruits_price_per_kg * fruits_total_kg

income_sales_lv = veggies_total_price_lv + fruits_total_price_lv
currency_rate = 1.94
income_veggies_fruits_eur = income_sales_lv / currency_rate

print(f'{income_veggies_fruits_eur:.2f}')

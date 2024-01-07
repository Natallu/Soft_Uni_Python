mackerel_price = float(input())     # скумрия
sprinkle_price = float(input())     # цаца
bonito_kg = float(input())          # паламуд
safrid_kg = float(input())
mussels_kg = float(input())         # миди

bonito_price_for_kg = mackerel_price + mackerel_price * 0.6
safrid_price_for_kg = sprinkle_price + sprinkle_price * 0.8

midi_total_price = mussels_kg * 7.50
bonito_total_price = bonito_kg * bonito_price_for_kg
safrid_total_price = safrid_kg * safrid_price_for_kg

fish_check = midi_total_price + bonito_total_price + safrid_total_price

print(f'{fish_check:.2f}')

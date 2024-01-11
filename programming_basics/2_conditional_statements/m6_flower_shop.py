import math

magnolias = int(input())
hyacinths = int(input())    # зюмбюли
roses = int(input())
cactus = int(input())
gift_price = float(input())

magnolias_tot = magnolias * 3.25
hyacinths_tot = hyacinths * 4
roses_tot = roses * 3.50
cactus_tot = cactus * 8
order_cost = magnolias_tot + hyacinths_tot + roses_tot + cactus_tot

tax_payment = order_cost - 0.05 * order_cost

money_left = abs(gift_price - tax_payment)

if tax_payment >= gift_price:
    print(f'She is left with {math.floor(money_left)} leva.')
else:
    print(f'She will have to borrow {math.ceil(money_left)} leva.')

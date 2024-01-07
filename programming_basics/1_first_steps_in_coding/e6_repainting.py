nylon = int(input())
paint = int(input())
thinner = int(input())
working_hours = int(input())

nylon_price = (nylon + 2) * 1.50
paint_price = (paint + paint * 0.1) * 14.50
thinner_price = thinner * 5
bag = 0.40

materials = paint_price + nylon_price + thinner_price + bag
painters_amount = (materials * 0.3) * working_hours

total_repainting_cost = materials + painters_amount

print(total_repainting_cost)

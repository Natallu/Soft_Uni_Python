flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs = int(input())
yeast = int(input())

sugar_price = flour_price - flour_price * 0.25
eggs_price = flour_price + flour_price * 0.10
yeast_price = sugar_price - sugar_price * 0.8

total = flour_kg * flour_price + sugar_kg * sugar_price + eggs * eggs_price + yeast * yeast_price

print(f"{total:.2f}")

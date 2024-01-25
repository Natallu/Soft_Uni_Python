age = int(input())
washing_machine = float(input())
price_per_toy = int(input())

toys = 0
money = 0
counter = 0

for _ in range(age):
    counter += 1
    if counter % 2 == 0:
        money += counter / 2 * 10
    else:
        toys += 1

toys_price = toys * price_per_toy
lilis_brother = age // 2
saved_money = money - lilis_brother + toys_price
diff = abs(washing_machine - saved_money)

if washing_machine <= saved_money:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')

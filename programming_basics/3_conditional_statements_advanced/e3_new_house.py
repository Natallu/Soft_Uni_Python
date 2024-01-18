flower = input()
flower_count = int(input())
budget = int(input())

price = 0

if flower == 'Roses':
    if flower_count <= 80:
        price = flower_count * 5
    else:
        roses = flower_count * 5
        price = roses - roses * 0.1
elif flower == 'Dahlias':
    if flower_count <= 90:
        price = flower_count * 3.8
    else:
        dahlias = flower_count * 3.8
        price = dahlias - dahlias * 0.15
elif flower == 'Tulips':
    if flower_count <= 80:
        price = flower_count * 2.8
    else:
        tulips = flower_count * 2.8
        price = tulips - tulips * 0.15
elif flower == 'Narcissus':
    if flower_count >= 120:
        price = flower_count * 3
    else:
        narcissus = flower_count * 3
        price = narcissus + narcissus * 0.15
elif flower == 'Gladiolus':
    if flower_count >= 80:
        price = flower_count * 2.5
    else:
        gladiolus = flower_count * 2.5
        price = gladiolus + gladiolus * 0.2

diff = abs(budget - price)

if price <= budget:
    print(f"Hey, you have a great garden with {flower_count} {flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")

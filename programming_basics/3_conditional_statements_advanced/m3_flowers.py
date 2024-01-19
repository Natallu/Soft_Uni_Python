chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

arran = 2
flowers = chrysanthemums + roses + tulips
h = 0
r = 0
t = 0

if season in ('Spring', 'Summer'):
    if holiday == 'N':
        h = chrysanthemums * 2
        r = roses * 4.10
        t = tulips * 2.50
    elif holiday == 'Y':
        h = chrysanthemums * 2 + chrysanthemums * 2 * 0.15
        r = roses * 4.10 + roses * 4.10 * 0.15
        t = tulips * 2.50 + tulips * 2.50 * 0.15
elif season in ('Autumn', 'Winter'):
    if holiday == 'N':
        h = chrysanthemums * 3.75
        r = roses * 4.5
        t = tulips * 4.15
    elif holiday == 'Y':
        h = chrysanthemums * 3.75 + chrysanthemums * 3.75 * 0.15
        r = roses * 4.5 + roses * 4.5 * 0.15
        t = tulips * 4.15 + tulips * 4.15 * 0.15

price = h + r + t
bouquet = 0

if tulips > 7 and season == 'Spring':
    bouquet = price - price * 0.05
elif roses >= 10 and season == 'Winter':
    bouquet = price - price * 0.1
else:
    bouquet = price

bouquet_1 = 0

if flowers > 20 and season in ('Spring', 'Summer', 'Autumn', 'Winter'):
    bouquet_1 = bouquet - bouquet * 0.2
else:
    bouquet_1 = bouquet

tot_bouquet = bouquet_1 + arran
print(f'{tot_bouquet:.2f}')

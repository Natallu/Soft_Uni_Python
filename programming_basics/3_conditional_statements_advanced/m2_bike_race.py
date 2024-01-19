juniors = int(input())
seniors = int(input())
trace = input()

participation_tax = 0
total_participants = juniors + seniors

if trace == 'trail':
    participation_tax = juniors * 5.50 + seniors * 7
elif trace == 'cross-country':
    if total_participants < 50:
        participation_tax = juniors * 8 + seniors * 9.50
    elif total_participants >= 50:
        participation_tax = (juniors * 8 + seniors * 9.50) - 0.25 * (juniors * 8 + seniors * 9.50)
elif trace == 'downhill':
    participation_tax = juniors * 12.25 + seniors * 13.75
elif trace == 'road':
    participation_tax = juniors * 20 + seniors * 21.5

expenses = participation_tax * 0.05

donation = participation_tax - expenses

print(f'{donation:.2f}')

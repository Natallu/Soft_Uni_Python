floors = int(input())
rooms = int(input())

for floor in reversed(range(1, floors + 1)):

    x = 'A' if floor % 2 else 'O'

    if floor == floors:
        x = 'L'

    for room in range(0, rooms):
        room_number = f'{x}{floor}{room}'
        print(room_number, end=' ')

    print()

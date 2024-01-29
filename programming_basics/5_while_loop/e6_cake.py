width = int(input())
length = int(input())

total_cake = width * length
pieces = total_cake
counter = 0

data = input()
while data != 'STOP':
    current_pieces = int(data)

    pieces -= current_pieces

    if pieces <= 0:
        break

    data = input()

diff = abs(pieces - counter)

if data == 'STOP' and pieces > counter:
    print(f'{diff} pieces are left.')
elif pieces <= counter:
    print(f'No more cake left! You need {diff} pieces more.')

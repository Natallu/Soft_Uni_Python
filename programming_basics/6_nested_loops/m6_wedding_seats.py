last_sector = input()
rows_first_sector = int(input())
odd_rows_seats = int(input())

sectors = ''
seat_counter = 0

for sector in range(ord('A'), ord(last_sector) + 1):
    sectors += chr(sector)

for index, sector in enumerate(sectors):

    for row in range(1, (rows_first_sector + index) + 1):
        if row % 2 != 0:
            for seat in range(ord('a'), ord('a') + odd_rows_seats):
                seat_counter += 1
                print(f'{sector}{row}{chr(seat)}')
        else:
            for seat in range(ord('a'), ord('a') + odd_rows_seats + 2):
                seat_counter += 1
                print(f'{sector}{row}{chr(seat)}')

print(seat_counter)

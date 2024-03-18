easter_breads = int(input())
top_points = 0
top_rated_baker = ''

for _ in range(easter_breads):
    baker = input()
    current_baker_points = 0

    while True:
        rate = input()

        if rate == 'Stop':
            print(f"{baker} has {current_baker_points} points.")
            if current_baker_points > top_points:
                top_rated_baker = baker
                top_points = current_baker_points
                print(f"{top_rated_baker} is the new number 1!")
            break

        current_baker_points += int(rate)

print(f"{top_rated_baker} won competition with {top_points} points!")

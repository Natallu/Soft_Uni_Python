men = int(input())
women = int(input())
tables = int(input())

for man in range(1, men + 1):
    for woman in range(1, women + 1):
        if tables == 0:
            break
        else:
            tables -= 1
            print(f'({man} <-> {woman})', end=" ")

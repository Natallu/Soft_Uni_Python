from math import ceil

wall_h = int(input())
wall_w = int(input())
windows_doors_p = int(input())

total = wall_h * wall_w * 4
windows_doors = total - windows_doors_p / 100 * total
paint_area = ceil(windows_doors)

data = input()
painted_counter = 0
while data != "Tired!":
    current_paint_l = int(data)

    painted_counter += current_paint_l

    if painted_counter >= paint_area:
        break

    data = input()

diff = abs(paint_area - painted_counter)
if data == 'Tired!':
    print(f"{diff} quadratic m left." )
elif painted_counter > paint_area:
    print(f"All walls are painted and you have {diff} l paint left!")
elif painted_counter == paint_area:
    print("All walls are painted! Great job, Pesho!" )
